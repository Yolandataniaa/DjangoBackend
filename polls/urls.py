from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('leaderboard/', views.home, name = 'home'),
    path('accounts/login/', views.login, name = 'login'),
    path('accounts/logout/', views.home, name = 'logout'),
    path('nilai/<int:number>/', views.nilai, name = 'nilai'),
    path('rapot/', views.rapot, name = 'rapot'),
    path('upload-csv/', views.upload, name='upload'),
]