## buddycloud website

Our static-site-generator should have the following features:

* Pretty URLS
* Support for Markdown (check)
* Google sitemap
* Active menus
* Publish to github pages (check)
* Quick Bootstrap (check)
* Live Preview (check)

### Requirements

* Pelican 3.3
* ghp-import
* Markdown 2.3.1

### Introduction to Pelican

Pelican's [GETTING STARTED](http://docs.getpelican.com/en/latest/getting_started.html/) page is a good place to learn about the basics of Pelican (installation, project skeleton, development cycle, etc.).

### Installation instructions
```bash
git clone ssh://git@github.com/buddycloud/buddycloud.com.git
# install Pelican and dependencies
cd buddycloud.com
```

### Runing the server in development mode

```bash
make serve
```

If you want the server to autoreload whenever a file change, you can instead do:

```bash
make devserver
```
View at `http://localhost:8000`

### Configuration

```
<repo>
  fabfile.py
  develop_server.sh
  Makefile
  README.md
  pelicanconf.py (development configuration)
  publishconf.py (production configuration)
  output
    <generated files - published to gh-pages branch>
  content
    pages
      <website page files>
  pelican-bootstrap3
    <website theme>
```

### Site generation

To just generate a new version (without starting up a local webserver) just do:

`make html`

### Publishing your changes

Files are updated to the `gh_pages` branch
```bash
make github
```
view the updates on http://new.buddycloud.com (and eventually buddycloud.com)
