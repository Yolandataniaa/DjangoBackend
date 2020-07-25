from django.urls import path
from . import views

urlpatterns = [
    path('upload/stat/', views.upload_stat, name='upload'),
    path('upload/marks/', views.upload_marks, name='uploadMarks'),
    path('upload/damage/', views.upload_damage, name='uploadDamage'),
    path('upload/user/', views.upload_user, name='uploadUser'),
    path('leaderboard/', views.leaderboard, name = 'leaderboard'),
    path('leaderboard-mingguan/', views.mingguan, name = 'mingguan'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.registerPage, name='register'),
    path('nilai/', views.nilai, name = 'nilai'),
    path('heal/', views.heal, name='heal'),
    path('', views.landing, name='landing')
]