from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExperienceListView.as_view(), name = 'experience-list'),
    path('<int:pk>/', views.ExperienceDetailView.as_view(), name = 'experience-detail'),
]