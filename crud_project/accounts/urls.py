from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import SingUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='acounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('signup/', SingUpView.as_view(), name='singup'),
    ]
