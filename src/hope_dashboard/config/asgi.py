import os

from django.core.asgi import get_asgi_application
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.core.handlers.asgi import ASGIHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hope_dashboard.config.settings")

application: ASGIHandler = get_asgi_application()
