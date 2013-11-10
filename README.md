## buddycloud website

### Requirements

* Ruby 1.9.3 or greater. Installation through RVM preferred.
* If you installed Ruby through RVM, create a gemset named `buddycloud`. 
* An .rvmrc file exists in the root of the project.

### Introduction to Middleman

Middleman's [GETTING STARTED](http://middlemanapp.com/getting-started/) page is a good place to learn about the basics of Middleman (installation, project skeleton, development cycle, etc.).

### Installation instructions
```bash
git clone git@github.com:buddycloud/buddycloud.com.git
# install Middleman and dependencies
bundle 
```

### Runing the server in development mode

```bash
middleman
```

The server autoreloads when files change.  View at `http://localhost:4567`

### Configuration

```
<repo>
  .rvmrc
  Gemfile
  Gemfile.lock
  README.md
  Rakefile
  config.rb
  build
    <generated files - published to gh-pages branch>
  source
    <website source files>
```

### Site generation

`middleman build` (use --clean to remove old files if necessary).

### Publishing your changes

Files are updated to the `gh_pages` branch
```bash
rake build
# publish to the gh_pages branch on https://github.com/buddycloud/buddycloud.com repo:
rake publish
```
view the updates on http://new.buddycloud.com (and eventually buddycloud.com)
