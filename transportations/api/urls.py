from django.urls import path
from transportations.api import views
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'airplane', AirplaneViewSet)

urlpatterns = []
urlpatterns += router.urls