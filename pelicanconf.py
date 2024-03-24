THEME = 'theme/basic'
AUTHOR = 'Miguel Boekhold'
SITENAME = 'Miguel Boekhold'
SITESUBTITLE = 'Coding the future, lifelong learning, and embracing creativity.'
SITEURL = ''
CUSTOM_CSS = 'static/custom.css'
PATH = 'content'
DEFAULT_METADATA = {
    'status': 'draft',
}
STATIC_PATHS = ['images/favicon.ico']
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}
}
TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

FAVICON = "static/images/favicon.ico"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True