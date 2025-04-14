from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('decrement_click/', views.decrement_click, name='decrement_click'),
    path('project_modal_content/<str:action>', views.project_modal_content, name='project_modal_content')


]
