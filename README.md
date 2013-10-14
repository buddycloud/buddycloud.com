## buddycloud website

### Requirements

* Ruby 1.9.3 or greater. Installation through RVM preferred.
* If you installed Ruby through RVM, create a gemset named `buddycloud`. An .rvmrc file exists in the root of the project.

### Gentle introduction to Middleman

Middleman is a Ruby static website generator. This means you can develop your static website using dynamic templates (ERB) but serve it in static fashion. ERB let's you use layouts, partials, url helpers (images, assets and links) and embed Ruby inside your HTML. During the build process (`$> middleman build`) all the ERB templates in the `/source` directory are compiled to static html and copied to the `/build` directory (which is not under version control).

### Installation instructions

* `$> git clone git@github.com:buddycloud/buddycloud.github.com.git`.
* `$> bundle` (install Middleman and dependencies)

### First steps

Middleman's [GETTING STARTED](http://middlemanapp.com/getting-started/) page is a good place to learn about the basics of Middleman (installation, project skeleton, development cycle, etc.).

### Runing the server in development mode 

* Run `$> middleman server` (or just `$> middleman`). The server autoreloads if configuration changes.
* Go to `http://localhost:4567`.

### Site generation

* `$> middleman build` (use --clean to remove old files if necessary). 

### Configuration

* Site configuration (like external extensions activation and configuration) resides in the `config.rb` file.