try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jay Zawrotny',
    'url': 'http://jayzawrotny.com/',
    'download_url': 'http:// .com',
    'author_email': 'jayzawrotny@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['MYAPP'],
    'scripts': [],
    'name': 'ex46'
}

setup(**config)
