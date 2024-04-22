# job_listing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/create/', views.job_create, name='job_create'),
    path('job/<int:pk>/update/', views.job_update, name='job_update'),
    path('job/<int:pk>/delete/', views.job_delete, name='job_delete'),
]
