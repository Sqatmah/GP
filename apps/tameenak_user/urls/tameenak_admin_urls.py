from django.urls import path
from apps.tameenak_user.views import tameenak_admin_views as views
app_name = 'tameenak_admin'

urlpatterns = [
    path('dashboard/', views.AdminDashboard.as_view(), name='admin_dashboard'),
    path('user-request/', views.AdminRequest.as_view(), name='user_request'),

]
