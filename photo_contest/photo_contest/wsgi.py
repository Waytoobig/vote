"""
WSGI project for photo_contest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path

# ensure staticfiles dir exists (avoids runtime warning from whitenoise)
_static_root = Path(__file__).resolve().parent.parent / "staticfiles"
_static_root.mkdir(parents=True, exist_ok=True)

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photo_contest.photo_contest.settings')
application = get_wsgi_application()
