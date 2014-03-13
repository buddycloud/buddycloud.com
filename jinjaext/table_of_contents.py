from xml.etree import ElementTree

class TableOfContents:

	hooks_taken = []

	@staticmethod
	def produce_new_hook(text):

		hook = text.strip().replace(" ", "_").lower()
		hook = hook.replace("/:", ":").replace("/", ":")
		hook = hook.replace(":", "_")
		hook = hook.replace(",", "").replace(".", "")
		if ( hook.startswith("_") ):
			hook = hook[1:]
		if ( hook.endswith("_") ):
			hook = hook[:-1]

		hook_base = hook
		hook_id = 2
		while (hook in TableOfContents.hooks_taken):

			hook = hook_base + "_" + str(hook_id)
			hook_id += 1

		print "producing", hook
		TableOfContents.hooks_taken.append(hook)
		return hook

	@staticmethod
	def consume_existing_hook(text):

		hook = text.strip().replace(" ", "_").lower()
		hook = hook.replace("/:", ":").replace("/", ":")
		hook = hook.replace(":", "_")
		hook = hook.replace(",", "").replace(".", "")
		if ( hook.startswith("_") ):
			hook = hook[1:]
		if ( hook.endswith("_") ):
			hook = hook[:-1]
		
		stub_hooks = map(lambda x: x[:x.rfind("_")], TableOfContents.hooks_taken)

		if hook[:hook.rfind("_")] in stub_hooks:
		
			hook_at = stub_hooks.index(hook[:hook.rfind("_")])
			print "@", hook_at
			hook = TableOfContents.hooks_taken[hook_at]
			print "$", hook
		
		TableOfContents.hooks_taken.remove(hook)
		print "consuming", hook
		return hook

	@staticmethod
	def extractTableOfContentsInfo(content):

		hooks_taken = []
		root = ElementTree.fromstring("<root>"+content+"</root>")

		toc_info = []

		def process(element):

			if ( element.tag == 'h1'
			  or element.tag == 'h2' ):
				toc_info.append({
					'tag' : element.tag,
					'text' : element.text,
					'hook' : TableOfContents.produce_new_hook(element.text)
				})
				print "produced: ", toc_info[-1]['hook']

			for child in element:
				process(child)

		process(root)
		return toc_info

	@staticmethod
	def createTableOfContents(toc_info):

		if ( len(toc_info) == 0 ):
			toc_html = ""
			return toc_html
		elif ( len(toc_info) == 1 ):
			toc_html = "<ul class='nav bs-sidenav'><li class='active'><a href='#%s' data-scroll data-url='true'>%s</a></li></ul>"
			toc_html %= (toc_info[0]['hook'], toc_info[0]['text'])
			return toc_html
		else:
			a_html = "<a href='#%s' data-scroll data-url='true'>%s</a>"
			toc_html = "<ul class='nav bs-sidenav'>"
			toc_html += "<li class='active'>"
			toc_html += a_html % (toc_info[0]['hook'], toc_info[0]['text'])
			last_tag = toc_info[0]['tag']
			for i in range(1,len(toc_info)):
				if ( toc_info[i]['tag'] == 'h1' ):
					if ( last_tag == 'h2' ):
						toc_html += "</ul>"
					toc_html += "</li>"
					toc_html += "<li>"
					toc_html += a_html % (toc_info[i]['hook'], toc_info[i]['text'])
				elif ( toc_info[i]['tag'] == 'h2' ):
					if ( last_tag == 'h1' ):
						toc_html += "<ul class='nav'>"
					toc_html += "<li>"
					toc_html += a_html % (toc_info[i]['hook'], toc_info[i]['text'])
					toc_html += "</li>"

				last_tag = toc_info[i]['tag']

			toc_html += "</ul>"
			return toc_html
	
	@staticmethod
	def addTableOfContentsHooks(content, toc_info):

		root = ElementTree.fromstring("<root>"+content+"</root>")

		def process(element):

			if ( element.tag == 'h1'
			  or element.tag == 'h2' ):
				element.attrib["id"] = TableOfContents.consume_existing_hook(element.text)
				print "consumed: ", element.attrib['id']

			for child in element:
				process(child)

		process(root)

		content = ElementTree.tostring(root, method="html")
		content = content.replace("<root>", "").replace("</root>", "") 
		return content
