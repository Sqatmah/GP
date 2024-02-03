from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.tameenak_user.views import tameenak_admin_views as views

app_name = 'tameenak_admin'

urlpatterns = [
    path('dashboard/', views.AdminDashboard.as_view(), name='admin_dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
