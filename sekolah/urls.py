from django.urls import path
from . import views
from . import upload

urlpatterns = [
    path('upload/stat/', upload.upload_stat, name='upload'),
    path('upload/marks/', upload.upload_marks, name='uploadMarks'),
    path('upload/damage/', upload.upload_damage, name='uploadDamage'),
    path('upload/potion/', upload.upload_potions, name='uploadPotion'),
    path('upload/user/', upload.upload_user, name='uploadUser'),
    path('leaderboard/', views.leaderboard, name = 'leaderboard'),
    path('leaderboard-mingguan/', views.mingguan, name = 'mingguan'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.registerPage, name='register'),
    path('nilai/', views.nilai, name = 'nilai'),
    path('heal/', views.heal, name='heal'),
    path('', views.landing, name='landing')
]