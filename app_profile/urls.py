from django.urls import path
from . import views

app_name = "app_profile"

urlpatterns = [
    path('', views.index, name='eng-home'),
    path('projects-details/', views.projects_details, name='eng-projects-details'),
    path('projects-details/<str:page>/', views.project_detail, name='eng-project-detail'),
    path('it/', views.index, name='it-home'),
    path('it/projects-details/', views.projects_details, name='it-projects-details'),
    path('it/projects-details/<str:page>/', views.project_detail, name='it-project-detail'),
]