from django.urls import path
from transportations.api import views


urlpatterns = [
    path('lists/', views.ListAirplane.as_view(), name='list_airplane')
]