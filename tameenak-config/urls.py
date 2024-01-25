from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tameenak_user/', admin.site.urls),
    path('tameenak_user/', include('apps.tameenak_user.urls')),
    path('insurance_company/', include('apps.insurance_company.urls')),
]
