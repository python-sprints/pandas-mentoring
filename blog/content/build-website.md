Title: Build a blog using Pelican
Date: 2019-09-08
Category: Tools
Tags: Pelican

## What is Pelican?
Pelican is a Python library that lets you generate static websites from templates.

## 1. Make a directory to host your site files
```
cd pandas-mentoring
mkdir blog
cd blog
```

## 2. Generate the initial boilerplate
```
pelican-quickstart

> Where do you want to create your new web site? [.]
> What will be the title of this web site? Pandas Mentoring Blog
> Who will be the author of this web site? Les Pandanistas
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) Y
> What is your URL prefix? (see above example; no trailing slash) https://python-sprints.github.io/pandas-mentoring
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris]
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) N
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
> Do you want to upload your website using Rackspace Cloud Files? (y/N) N
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) N
Done. Your new project is available at localpath/pandas-mentoring/blog
```

## 3. Add content in a markdown file
```
vim content/build-blog.md
```

## 4. Generate and preview your site
```
pelican content
pelican --listen
# Navigate to http://localhost:8000/ in your browser.
```

## 5. Add a theme
```
# Choose a path to clone pelican-themes directory (e.g. blog/)
git clone --recursive https://github.com/getpelican/pelican-themes ../pelican-themes

# Add a theme in the pelicanconf.py of your site (e.g. fishingbird/pelicanconf.py)
THEME = '../pelican-themes/uikit'
```

## 7. Publish to your Github project page
```
# Open pelicanconf.py
vim pelicanconf.py

# Add your SITE_URL
SITEURL = 'https://python-sprints.github.io/pandas-mentoring'

# Save your file
```
```
# Generate output
pelican content -o home -s pelicanconf.py

# Publish to GitHub using ghp-import
ghp-import home -n

# Push to gh-pages branch
git push origin gh-pages
```

## 8. What are the files?
  * Makefile - This file defines make commands that perform the most important tasks like generating your site and starting a local http server.
  * pelicanconf.py - This file contains settings to customize your site.
  * publishconf.py - This file contains settings that are only used when you’re ready to publish to the web.
  * content/ - This folder is where you’ll put the templates and files that will be translated into the content of your site.
  * home/ - This folder might not exist until you convert your content into html. By default, the translated website lands here.


## 9. Reference
  * [Tutorials](https://github.com/getpelican/pelican/wiki/Tutorials)
  * [Documentation](https://docs.getpelican.com/en/stable/)
