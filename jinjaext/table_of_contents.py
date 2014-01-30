from xml.etree import ElementTree


def extractTableOfContentsInfo(content):

	tree = ElementTree.fromstring("<root>"+content+"</root>")

	toc = []

	def process(element):
		global toc

		if ( element.tag == 'h1'
		  or element.tag == 'h2'
		  or element.tag == 'h3' ):
			#generate a unique id from the text
			#and place it here as well
			toc.append((element.tag, element.text))

	process(tree.getroot())

	return toc

def createTableOfContents(toc_info):
	return ""

def addTableOfContentsHooks(content, toc_info):
	return content
