from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'mailings', views.MailingViewSet, basename='mailing')
router.register(r'customers', views.CustomerViewSet, basename='customer')
router.register(r'operators', views.OperatorViewSet, basename='operator')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'messages', views.MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls))
]
