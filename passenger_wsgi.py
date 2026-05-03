import os
import sys

# Add project to path
sys.path.insert(0, os.path.dirname(__file__))

# Set settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'zltProfile.settings.prod'

from zltProfile.wsgi import application
