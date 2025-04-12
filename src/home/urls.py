from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('increment/', views.increment_click, name='increment_click'),

]