import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROD = False
SQLITE = True
POSTGRES = False

def get_database():
  if SQLITE:
    return {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': BASE_DIR / 'db.sqlite3',
    }
  else:
    if POSTGRES:
      return {
        'ENGINE': 'django.db.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432'
      }
    else:
      return {
        'ENGINE': 'django.db.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432'
      }