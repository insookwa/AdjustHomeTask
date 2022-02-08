from django import views
from django.urls import path,include
from .views import DataAPIView

urlpatterns = [
    path('adjust/', DataAPIView.as_view() ,name = 'all-data')
]