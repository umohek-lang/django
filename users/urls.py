from django.urls import path, include
from users import views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('users/signup', views.signup, name='signup'),
    path('users/profile', views.profile, name='profile'),
    path('users/confirm/logout', views.logoutconfirm, name='logoutconfirm'),

    # Login Url
    path('users/login',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),


     path(
        'users/logout',
        auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
     path(
        'users/password_reset',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'
    ),
     path(
        'users/password_reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),
     path(
        'users/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
     path(
        'users/reset/done',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
   
