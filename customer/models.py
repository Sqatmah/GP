from django.db import models
from django.contrib.auth.models import User
from datetime import date
from .constant import *

class Base(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        abstract = True 

class Role(Base):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

class Address(Base):
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.street} / {self.city} / {self.state}"
    
class Users(Base):
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    name_company = models.CharField(
        max_length=255, 
        null=True, 
        blank=True
        )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    ex_subscription = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        choices = EX_SUBSCRIPTION
    )
    phone = models.CharField(
        max_length=255,
        null=True,
        blank=True
        )
    user_status = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices = USER_STATUS,
    )
    gender = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices = GENDERS,
    )
    blood = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    allergies = models.TextField()
    medical_condition = models.TextField(
        null=True,
        blank=True
    )
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    
class InsuranceCompany(Base):
    name = models.CharField(max_length=256, null=True, blank=True)
    logo = models.ImageField(
        upload_to='mediafile',
        verbose_name="Logo",
    )
    description = models.TextField(max_length=255, null=True, blank=True)
    pdf = models.CharField(max_length=255, null=True, blank=True)
    address_id = models.IntegerField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    establishment = models.DateField()
    degrees = models.CharField(
        max_length=255,
        null=True, 
        blank=True,
        choices = INSURANCE_DEGREE
    )
    def __str__(self) -> str:
        return f"{self.name}"
    

class Payments(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    insurance_company = models.OneToOneField(InsuranceCompany, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.CharField(
        max_length=255,
        null=True, 
        blank=True
        )
    payments_status = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices = PAYMENT_STATUS
    )

    def __str__(self) -> str:
        return f"{self.user} paid for {self.insurance_company}"

class Requests(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, null=True, blank=True)
    request_status = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices = REQUEST_STATUS
    )

    def __str__(self) -> str:
        return f"{self.user} request to {self.insurance_company} and status is {self.request_status}"
    

class MedicalProfile(Base):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True, blank=True)
    medical_history = models.TextField(
        null=True,
        blank=True
    )
    current_madications = models.TextField(
        null=True,
        blank=True
    )
    allergeis = models.TextField(
        null=True,
        blank=True
    )
    family_medical = models.TextField(
        null=True, 
        blank=True
    )
    history = models.TextField(
        null=True,
        blank=True
    )
    lifestyle_factors = models.TextField(
        null=True,
        blank=True
    )
    chronic_conditions = models.TextField(
        null=True,
        blank=True
    )
    special = models.TextField(
        null=True,
        blank=True
    )
    considerations = models.TextField(
        null=True,
        blank=True
    )