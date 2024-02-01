from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Address(BaseModel):
    street = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    postal_code = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.street} - {self.city} - {self.country} - {self.postal_code}"
