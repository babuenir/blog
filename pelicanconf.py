#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'BabuSubashChandar'
SITENAME = u'BabuSubashChandar'
SITETITLE = u'Babuenir'
SITESUBTITLE = u'Random musings on Technology, Art & Science'
SITEURL = u'https://babuenir.github.io/blog'
GRAVATAR_IMAGE = 'https://secure.gravatar.com/avatar/aaf9dadf96ba3361de25e04a6c9fdfc3'
SITELOGO = SITEURL + u'/static/images/babuenir.png'

DISQUS_SITENAME = u'babuenir'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

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
SOCIAL = (('Github', 'https://github.com/babuenir'),
          ('Twitter', 'https://twitter.com/babuenir'),
          ('Linkedin', 'https://www.linkedin.com/in/babuenir'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ABOUT = """BabuSubashChandar is an Open Source Software enthusiast,
Embedded Systems Engineer and trainer by profession, an ardent lover of
arts and science. This is his personal blog, where you can find his
experiences and works related to GNU/Linux, Embedded Systems,
Literature, Paintings, and so on. He is currently living in Chennai,
India.
"""

STATIC_PATHS = ['static', ]

THEME = "theme"

ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
