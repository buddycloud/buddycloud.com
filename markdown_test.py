import markdown, sys, os

md = markdown.Markdown(extensions=["mdext.togglable_tabs"])

md.convertFile(sys.argv[1], "output.md")
