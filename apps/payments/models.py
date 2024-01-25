from django.db import models
from apps.tameenak_user.models import TameenakCustomer
from apps.insurance_company.models import InsuranceCompany
from apps.main.models import (
    BaseModel,
    Address
)
from apps.payments.constants import PAYMENT_STATUS


class Payments(BaseModel):
    customer = models.ForeignKey(
        TameenakCustomer,
        on_delete=models.CASCADE
    )
    insurance_company = models.ForeignKey(
        InsuranceCompany,
        on_delete=models.CASCADE
    )
    amount = models.FloatField(
        null=True,
        blank=True,
    )
    payment_date = models.DateField(
        null=True,
        blank=True,
    )
    payment_status = models.CharField(
        choices=PAYMENT_STATUS,
        max_length=50,
        null=True,
        blank=True,
    )

    def __str__(self):
        return (
            f"{self.customer.user.first_name} / "
            f"{self.insurance_company.name} / "
            f"{self.amount} / {self.payment_date} / "
            f"{self.payment_status}"
        )
