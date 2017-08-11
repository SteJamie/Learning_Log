"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
# recommended in the book for heroku :
# from dj_static import Cling
# recommended on heroku's website
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
application = DjangoWhiteNoise(get_wsgi_application())