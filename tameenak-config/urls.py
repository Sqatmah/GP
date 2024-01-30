from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.urls import (
    path,
    include
)

urlpatterns = [
    path('tameenak-super-admin/', admin.site.urls),
    path('tameenak-user/', include('apps.tameenak_user.urls.tameenak_user_urls', namespace='tameenak_user')),
    path('tameenak-admin/', include('apps.tameenak_user.urls.tameenak_admin_urls', namespace='tameenak_admin')),
    path('insurance-co/', include('apps.insurance_company.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
