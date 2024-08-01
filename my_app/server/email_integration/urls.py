from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmailAccountViewSet, message_list

router = DefaultRouter()
router.register(r'email-accounts', EmailAccountViewSet)

urlpatterns = [
    path('messages/', message_list, name='message_list'),
    path('', include(router.urls)),
]