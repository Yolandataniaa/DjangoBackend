from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('leaderboard/', views.leaderboard, name = 'leaderboard'),
    path('nilai/', views.nilai, name = 'nilai'),
    path('rapot/', views.rapot, name = 'rapot'),
    path('upload-csv/', views.upload, name='upload'),
]