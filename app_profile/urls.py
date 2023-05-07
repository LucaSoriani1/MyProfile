from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_eng, name='home_eng'),
    path('projects-details/', views.projects_details_eng, name='projects-details-eng'),
    path('projects-details/<int:id>/', views.project_detail_eng, name='project-detail-eng'),
    path('it/', views.index_it, name='home_it'),
    path('it/projects-details/', views.projects_details_it, name='projects-details-it'),
    path('it/projects-details/<int:id>/', views.project_detail_it, name='project-detail-it'),
]