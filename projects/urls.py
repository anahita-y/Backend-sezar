from django.urls import path
from . import views

urlpatterns = [
    path('technologies/', views.TechnologyListView.as_view(), name = 'technologies'),
    path('', views.ProjectListView.as_view(), name = 'project-list'),
    path('<int:pk>/',views.ProjectDetailView.as_view(), name = 'project-detail'),

]