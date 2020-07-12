from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.leaderboard, name = 'leaderboard'),
    path('nilai/', views.nilai, name = 'nilai'),
    path('upload-csv/', views.upload, name='upload'),
    path('register/', views.registerPage, name='register'),
    path('profile/', views.profile, name='profile'),
    path('upload-user/', views.uploadUser, name='uploadUser'),
    path('', views.landing, name='landing')
]