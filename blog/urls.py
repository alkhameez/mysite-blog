from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),


    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='login_form.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='logout_form.html'), name='logout'),


    path('password-change', views.pass_change, name='password_change'),
    path('password_change_done', views.password_change_done, name='password_change_done'),


    path('password_reset', views.password_reset, name='password_reset'),
    path('password_reset_confirm', views.password_reset_confirm, name='password_reset_confirm'),
]
