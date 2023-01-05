from django.urls import path
from residences.api import views
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'airplane', HotelRoomViewSet)

urlpatterns = []
urlpatterns += router.urls
