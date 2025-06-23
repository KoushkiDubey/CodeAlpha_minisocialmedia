from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='core/auth/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='core/auth/login.html',
        next_page='login'
    ), name='logout'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # Removed username parameter
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('like-post/', views.like_post, name='like_post'),
    path('explore/', views.explore, name='explore'),
]