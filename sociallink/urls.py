from django.urls import path
from . import views

urlpatterns = [
    path('', views.SocialLinkListView.as_view(), name = 'sociallink-list'),
]