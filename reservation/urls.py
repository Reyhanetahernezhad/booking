from django.urls import path
from residences.api import views

urlpatterns = [
    path('lists/', views.List.as_view(), name='list_Room')
]