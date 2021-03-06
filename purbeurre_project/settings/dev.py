"""
Django settings for purbeurre_project project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("PURBEURRE_SECRET_KEY", "idsqn%qsm!dfihzq@zml-fpvn9s_qdf")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PURBEURRE_DBNAME", "purbeurre_dbname"),
        "USER": os.environ.get("PURBEURRE_DBUSER", "purbeurre_dbuser"),
        "PASSWORD": os.environ.get("PURBEURRE_DBPASSWD", "purbeurre_dbpasswd"),
        "HOST": "localhost",
        "PORT": 5432,
    }
}
