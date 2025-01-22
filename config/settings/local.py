"""
Local development settings.
"""
from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d^)9wf*w_(q$hv$vf3=s9j0&u_dq*u&fkc--88qwv55y#11%bm'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Additional local development apps
INSTALLED_APPS += [
    'django_extensions',  # Useful development tools
    'debug_toolbar',      # Django Debug Toolbar
]

# Django Debug Toolbar
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1'] 