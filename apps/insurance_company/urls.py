from django.urls import path
from apps.insurance_company import views
from django.contrib.auth.views import (
    LogoutView,
    LoginView
)

app_name = 'insurance_company'

urlpatterns = [
    # path('', views.home_view, name=''),
    # path('logout', LogoutView.as_view(template_name='insurance_company/logout.html'), name='logout'),
    # path('aboutus', views.aboutus_view),
    # path('contactus', views.contactus_view),
    # path('afterlogin', views.afterlogin_view, name='afterlogin'),
    #
    # path('adminlogin', LoginView.as_view(template_name='insurance_company/adminlogin.html'), name='adminlogin'),
    # path('tameenak_user-dashboard', views.admin_dashboard_view, name='tameenak_user-dashboard'),
    #
    # path('tameenak_user-view-tameenak_user', views.admin_view_customer_view, name='tameenak_user-view-tameenak_user'),
    # path('update-tameenak_user/<int:pk>', views.update_customer_view, name='update-tameenak_user'),
    # path('delete-tameenak_user/<int:pk>', views.delete_customer_view, name='delete-tameenak_user'),
    #
    # path('tameenak_user-category', views.admin_category_view, name='tameenak_user-category'),
    # path('tameenak_user-view-category', views.admin_view_category_view, name='tameenak_user-view-category'),
    # path('tameenak_user-update-category', views.admin_update_category_view, name='tameenak_user-update-category'),
    # path('update-category/<int:pk>', views.update_category_view, name='update-category'),
    # path('tameenak_user-add-category', views.admin_add_category_view, name='tameenak_user-add-category'),
    # path('tameenak_user-delete-category', views.admin_delete_category_view, name='tameenak_user-delete-category'),
    # path('delete-category/<int:pk>', views.delete_category_view, name='delete-category'),
    #
    # path('tameenak_user-policy', views.admin_policy_view, name='tameenak_user-policy'),
    # path('tameenak_user-add-policy', views.admin_add_policy_view, name='tameenak_user-add-policy'),
    # path('tameenak_user-view-policy', views.admin_view_policy_view, name='tameenak_user-view-policy'),
    # path('tameenak_user-update-policy', views.admin_update_policy_view, name='tameenak_user-update-policy'),
    # path('update-policy/<int:pk>', views.update_policy_view, name='update-policy'),
    # path('tameenak_user-delete-policy', views.admin_delete_policy_view, name='tameenak_user-delete-policy'),
    # path('delete-policy/<int:pk>', views.delete_policy_view, name='delete-policy'),
    #
    # path('tameenak_user-view-policy-holder', views.admin_view_policy_holder_view,
    #      name='tameenak_user-view-policy-holder'),
    # path('tameenak_user-view-approved-policy-holder', views.admin_view_approved_policy_holder_view,
    #      name='tameenak_user-view-approved-policy-holder'),
    # path('tameenak_user-view-disapproved-policy-holder', views.admin_view_disapproved_policy_holder_view,
    #      name='tameenak_user-view-disapproved-policy-holder'),
    # path('tameenak_user-view-waiting-policy-holder', views.admin_view_waiting_policy_holder_view,
    #      name='tameenak_user-view-waiting-policy-holder'),
    # path('approve-request/<int:pk>', views.approve_request_view, name='approve-request'),
    # path('reject-request/<int:pk>', views.disapprove_request_view, name='reject-request'),
    #
    # path('tameenak_user-question', views.admin_question_view, name='tameenak_user-question'),
    # path('update-question/<int:pk>', views.update_question_view, name='update-question'),

]
