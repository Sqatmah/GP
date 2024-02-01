from django.urls import path
from apps.tameenak_user.views import tameenak_user_views as views
from django.contrib.auth.views import LoginView

app_name = 'tameenak_user'

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='register'),
    path('dashboard/', views.UserDashboard.as_view(), name='dashboard'),
    path('request-insurance/<int:pk>', views.RequestInsurance.as_view(), name='request_insurance'),
    path('medical-profile/', views.MedicalProfile.as_view(), name='medical_profile'),
    path('user-history/', views.UserHistory.as_view(), name='user_history'),
]