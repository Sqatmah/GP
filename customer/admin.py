from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Role)
admin.site.register(Users)
admin.site.register(Address)
admin.site.register(InsuranceCompany)
admin.site.register(Payments)
admin.site.register(Requests)
admin.site.register(MedicalProfile)