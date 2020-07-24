from django.urls import path
from . import views

urlpatterns = [
    path('upload-csv/', views.upload, name='upload'),
    path('upload-user/', views.uploadUser, name='uploadUser'),
    path('leaderboard/', views.leaderboard, name = 'leaderboard'),
    path('leaderboard-mingguan/', views.mingguan, name = 'mingguan'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.registerPage, name='register'),
    path('nilai/', views.nilai, name = 'nilai'),
    path('heal/', views.heal, name='heal'),
    path('', views.landing, name='landing')
]