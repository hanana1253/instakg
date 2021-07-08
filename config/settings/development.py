from pathlib import Path
import os

DEBUG = True

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]

ALLOWED_HOSTS = ['0.0.0.0', 'production']
