import subprocess, logging, os, errno, codecs
from itertools import chain
from pelican import signals
from pelican.readers import BaseReader
from pelican.generators import PagesGenerator
from pelican.contents import Page, is_valid_content


logger = logging.getLogger(__name__)


class SlateReader(BaseReader):
    enabled = True
    file_extensions = ['slate', 'slt', 'sl8']

    def read(self, source_path):

        source = codecs.open(source_path, 'r')

        metadata = {}
        line = source.readline()
        while ( line.strip() != "" ):
            name = line.split(":")[0].strip().lower()
            value = line.split(":")[1].strip()
            metadata[name] = self.process_metadata(name, value)
            line = source.readline()

        content = source.read()
        source.close()

        slate_content = codecs.open('slate/source/index.md', 'w')
        slate_content.write(content)
        slate_content.close()
        os.chdir(os.path.join(os.getcwd(), "slate"))

        p = subprocess.Popen(
            ['bundle', 'exec', 'middleman', 'build', '--clean'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = p.communicate()
        if ( p.returncode != 0 ):
            raise Exception(err)

        slate_content = codecs.open('build/index.html', 'r')
        processed = slate_content.read()
        processed = processed.decode('utf-8')
        slate_content.close()
        os.chdir("../")

        print processed

        return processed, metadata

def add_reader(readers):
    readers.reader_classes['slate'] = SlateReader

def register():
    signals.readers_init.connect(add_reader)

def _make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

class SlatePage(Page):
    default_template = 'slate_page'

class SlateGenerator(PagesGenerator):

    def __init__(self, pages_generator):
##    def __init__(self, pelican_object):
##        context = pelican_object.settings.copy()
##        context['filenames'] = {}
##        context['localsiteurl'] = pelican_object.settings['SITEURL']
##        generators = [
##            cls(
##                context = context,
##                settings = pelican_object.settings,
##                path = pelican_object.path,
##                theme = pelican_object.theme,
##                output_path = pelican_object.output_path,
##            ) for cls in pelican_object.get_generator_classes()
##        ]

##        pages_generator = next(g for g in generators
##                              if isinstance(g, PagesGenerator))
        self.generator = pages_generator

    def generate(self):

        for f in self.generator.get_files(
            self.generator.settings['SLATE_PAGES_DIR']):
            try:

                page = self.generator.readers.read_file(
                    base_path = self.generator.path, path = f,
                    content_class = SlatePage, context = self.generator.context)

                _make_sure_path_exists("output/theme/vendor")

#                p = subprocess.Popen(['cp',
#                    'slate/build/index.html',
#                    'output/' + page.save_as.strip()])
#                out, err = p.communicate()
#                if ( p.returncode != 0 ):
#                    raise Exception(err)

                p = subprocess.Popen(['cp', '-R',
                    'slate/build/theme/vendor/slate',
                    'output/theme/vendor/slate'])
                out, err = p.communicate()
                if ( p.returncode != 0 ):
                    raise Exception(err)

            except Exception as e:
                logger.warning('Could not process {}\n{}'.format(f, e))
                continue
            else:

#                if not is_valid_content(page, f):
#                   continue

                self.generator.add_source_path(page)

                if page.status == "published":
                    self.generator.pages.append(page)
                else:
                    logger.warning("Unknown status %s for file %s," +
                        " skipping it." % (repr(page.status), repr(f)))

        self.generator._update_context(('pages', ))
        self.generator.context['PAGES'] = self.generator.pages

def generate_slate_pages_too(pelican_object):
    slate_generator = SlateGenerator(pelican_object)
    slate_generator.generate()

signals.page_generator_finalized.connect(generate_slate_pages_too)
