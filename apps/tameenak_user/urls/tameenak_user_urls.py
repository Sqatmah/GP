from django.urls import path
from apps.tameenak_user.views import tameenak_user_views as views
from django.contrib.auth.views import LoginView

app_name = 'tameenak_user'

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
]