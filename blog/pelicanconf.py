#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Les Pandanistas'
SITENAME = 'Blog'
#SITEURL = 'https://python-sprints.github.io/pandas-mentoring'
PATH = 'content'
OUTPUT_PATH = 'home'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pandas', 'https://pandas-docs.github.io/pandas-docs-travis/'),
        ('Python Sprints', 'https://python-sprints.github.io/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/python-sprints/pandas-mentoring'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Add a theme
THEME = '../pelican-themes/uikit'
DISPLAY_TAGS_ON_SIDEBAR_LIMIT = 0
DISPLAY_LINKS_ON_SIDEBAR_LIMIT = 0
LICENSE = {
    'cc_name': "by-sa",
    'hosted': False,
    'compact': True,
    'brief': False
    }
AUTHOR_IMAGE = '../img/logo.jpeg'
