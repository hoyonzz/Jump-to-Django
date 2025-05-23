from django.urls import path
from django.contrib.auth import views as auth_view
from . import views


app_name = 'common'


urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
