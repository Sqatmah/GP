from django.db import models
from apps.main.models import (
    BaseModel,
    Address
)


class InsuranceDegree(BaseModel):
    degree_type = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.degree_type}"


class InsuranceCompany(BaseModel):
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE
    )
    insurance_degree = models.ForeignKey(
        InsuranceDegree,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    logo = models.ImageField(
        upload_to='image/insurance_company/logo',
        default='image/insurance_company/logo/default_logo.png'
    )
    email = models.EmailField(
        max_length=100,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    website = models.URLField(
        max_length=200,
        null=True,
        blank=True,
    )
    capital = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    established_date = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} / {self.insurance_degree}"
