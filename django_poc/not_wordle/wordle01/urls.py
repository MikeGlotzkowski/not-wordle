from django.urls import path

from . import views
app_name = 'wordle01'
urlpatterns = [
    path('', views.index, name='index'),
]