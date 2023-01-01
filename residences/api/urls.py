from django.urls import path
from residences.api import views

urlpatterns = [
    path('lists/', views.RoomList.as_view(), name='list_Room')
]