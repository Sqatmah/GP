from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('homepage/', views.HomePage.as_view(), name='home_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.customer_signup_view, name='signup/'),
    path('dashboard/', views.customer_dashboard_view, name='dashboard'),
    path('search/', views.search_form, name='search_view'),
    path('medical-profile/', views.medical_profile_form, name='medical_profile_form'),
    path('medical-profile/success/', views.medical_profile_form_success, name='medical_profile_form_success'),
    path('submit_record/', views.submit_record_view, name='submit_record'),
]