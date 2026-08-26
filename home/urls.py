from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('documents/',views.SiteDocumentListView.as_view() , name = 'documents'),
]