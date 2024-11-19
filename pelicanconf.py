THEME = 'theme/basic'
AUTHOR = 'Miguel Boekhold'
SITENAME = 'Miguel Boekhold'
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

TEMPLATE_PAGES = {'paintings.html': 'paintings.html', "projects.html": "projects.html", "about.html": "about.html"}
STATIC_PATHS = ['static', 'images/paintings']
PAINTINGS = [
    'images/paintings/lake_with_tree.jpeg',
    'images/paintings/blue_dog.jpeg',
]
PROJECTS = [
    {
        "title": "Early Moves",
        "description": "This is a project",
        "image": "images/paintings/lake_with_tree.jpeg",
        "url": "https://www.google.com"
    },
    {
        "title": "Cry Detection",
        "description": "This is a project",
        "image": "images/paintings/blue_dog.jpeg",
        "url": "https://www.google.com"
    }
]