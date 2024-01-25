from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'tameenak_user'

urlpatterns = [
    path('customerclick', views.customerclick_view, name='customerclick'),
    path('customersignup', views.customer_signup_view, name='customersignup'),
    path('tameenak_user-dashboard', views.customer_dashboard_view, name='tameenak_user-dashboard'),
    path('customerlogin', LoginView.as_view(template_name='apps/templates/insurance/adminlogin.html'),
         name='customerlogin'
         ),
    path('apply-policy', views.apply_policy_view, name='apply-policy'),
    path('apply/<int:pk>', views.apply_view, name='apply'),
    path('history', views.history_view, name='history'),

    path('ask-question', views.ask_question_view, name='ask-question'),
    path('question-history', views.question_history_view, name='question-history'),
]
