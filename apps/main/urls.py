from django.urls import path
from apps.main import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

