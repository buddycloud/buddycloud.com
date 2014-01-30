from xml.etree import ElementTree

class TableOfContents:

	def __init__(self):
		self.hooks_taken = []

	def produce_new_hook(self, text):

		hook = text.strip().replace(" ", "_").lower()

		hook_base = hook
		hook_id = 2
		while (hook in self.hooks_taken):

			hook = hook_base + "_" + str(hook_id)
			hook_id += 1

		self.hooks_taken.append(hook)
		return hook

	def consume_existing_hook(self, text):

		hook = text.strip().replace(" ", "_").lower()
		stub_hooks = map(lambda x: x[:x.rfind("_")], self.hooks_taken)

		if hook[:hook.rfind("_")] in stub_hooks:
		
			hook_at = stub_hooks.index(hook[:hook.rfind("_")])
			hook = self.hooks_taken[hook_at]
			self.hooks_taken.remove(hook)

		return hook

	@staticmethod
	def extractTableOfContentsInfo(content):

		root = ElementTree.fromstring("<root>"+content+"</root>")

		toc_info = []

		def process(element):
			global toc

			if ( element.tag == 'h1'
			  or element.tag == 'h2'
			  or element.tag == 'h3' ):
				toc_info.append({
					'tag' : element.tag,
					'text' : element.text,
					'hook' : self.produce_new_hook(text)
				})

		process(root)

		return toc_info

	@staticmethod
	def createTableOfContents(toc_info):

		toc_html = ""
		if ( len(toc_info) == 0 ):
			return toc_html
		elif ( len(toc_info) == 1 ):
			toc_html = "<ul><li><a href='#%s' class='smoothScroll'>%s</a></li></ul>"
			toc_html %= (toc_info[0]['hook'], toc_info[0]['text'])
			return toc_html
		else:
			toc_html = "<ul><li><a href='#%s' class='smoothScroll'>%s</a></li></ul>"
			toc_html %= (toc_info[0]['hook'], toc_info[0]['text'])
			return toc_html
	
	@staticmethod
	def addTableOfContentsHooks(content, toc_info):
		return content
