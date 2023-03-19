from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('story1', views.Story1, name="story1"),
]