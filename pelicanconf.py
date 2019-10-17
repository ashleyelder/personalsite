#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ashley'
SITENAME = u'Ashley Elder'
SITESUBTITLE = u'welcome to my personal website'
SITEURL = ''

HEADER_COVER = 'https://raw.githubusercontent.com/ashleyelder/fileHosting/master/eldorado.png'

PATH = 'content'

DEFAULT_DATE_FORMAT = '%d %b %Y'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/ashleyelder'),
          ('linkedin','https://www.linkedin.com/in/ashleyelder'))

DEFAULT_PAGINATION = 5

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'attila-1.3'

AUTHORS_BIO = {
  "ashley": {
    "name": "Ashley",
    # "cover": "https://raw.githubusercontent.com/ashleyelder/fileHosting/master/eldorado.png",
    "image": "/images/avatar.png",
    "website": "http://ashleyelder.net",
    "linkedin": "ashleyelder",
    "github": "ashleyelder",
    "location": "Boulder, CO, USA",
    "bio": "Full stack developer particularly interested in developing software that scales with best practices. I enjoy building things."
  }
}