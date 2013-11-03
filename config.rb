###
# Page options, layouts, aliases and proxies
###

# Per-page layout changes:

with_layout :page_layout do
  page "*.html"
end

page "/index.html", layout: :home_layout

# Proxy pages (http://middlemanapp.com/dynamic-pages/)
# proxy "/this-page-has-no-template.html", "/template-file.html", :locals => {
#  :which_fake_page => "Rendering a fake page with a local variable" }

###
# Helpers
###

helpers do

  def nav_link_to(title, path, options = {})
    if current_resource.url.index(url_for(path))
      options[:class] = options[:class].to_s + " active"
    end
    link_to(title, path, options)
  end
end

# Automatic image dimensions on image_tag helper
# activate :automatic_image_sizes

# Reload the browser automatically whenever files change
activate :livereload

# Methods defined in the helpers block are available in templates
# helpers do
#   def some_helper
#     "Helping"
#   end
# end

set :css_dir, 'css'

set :js_dir, 'js'

set :images_dir, 'img'

# Activate Pretty URLs (Directory Indexes)
activate :directory_indexes

# Activate Syntax Highlighter
activate :syntax

# Set Markdown Engine
set :markdown_engine, :kramdown

set :relative_links, true

# Build-specific configuration
configure :build do
  # For example, change the Compass output style for deployment
  activate :minify_css

  # Minify Javascript on build
  activate :minify_javascript

  # Enable cache buster
  # activate :asset_hash

  # Use relative URLs
  activate :relative_assets

  # Or use a different image path
  # set :http_prefix, "/Content/images/"
end
