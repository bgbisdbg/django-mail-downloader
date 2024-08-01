from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/email_import/$', consumers.EmailImportConsumer.as_asgi()),
]