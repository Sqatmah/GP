from django.contrib import admin
from django.urls import (
    path,
    include
)

urlpatterns = [
    path('tameenak-super-admin', admin.site.urls),
    path('', include('apps.main.urls')),
    path('tameenak-user/', include('apps.tameenak_user.urls.tameenak_user_urls', namespace='tameenak_user')),
    path('tameenak-admin/', include('apps.tameenak_user.urls.tameenak_admin_urls', namespace='tameenak_admin')),
    path('insurance-co/', include('apps.insurance_company.urls')),
]
