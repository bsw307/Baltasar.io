#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'baltasar'
SITENAME = 'Sequoia'
SITEURL = ''
GITHUB_URL = "https://github.com/Baltasaurus"
PATH = 'content'
THEME = "theme"

STATIC_PATHS = ['img']
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['gallery']

GALLERY_PATH = 'img/gallery/'

TAG_SAVE_AS = '{slug}.html'
TAG_URL = '{slug}.html'

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True