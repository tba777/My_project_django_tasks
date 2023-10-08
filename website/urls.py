from django.urls import path
from . import views


# app_name = 'website'  # Это добавьте для уточнения пространства имен приложения Но я убрал чтоб не давало ошибку


urlpatterns = [
    path('', views.home_page, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    ]
