from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']

# Email to console in dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files - don't collect in dev
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
