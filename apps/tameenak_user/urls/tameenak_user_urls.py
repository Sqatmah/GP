from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.tameenak_user.views import tameenak_user_views as views
from django.contrib.auth.views import LoginView

app_name = 'tameenak_user'

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='register'),
    path('dashboard/', views.UserDashboard.as_view(), name='user_dashboard'),
    path('request-insurance/<int:pk>', views.RequestInsurance.as_view(), name='request_insurance'),
    path('download-insurance-details/<int:pk>', views.DownloadInsuranceDetails.as_view(),
         name='download_insurance_details'),
    path('medical-profile/', views.MedicalProfileView.as_view(), name='medical_profile'),
    path('user-history/', views.UserHistory.as_view(), name='user_history'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
