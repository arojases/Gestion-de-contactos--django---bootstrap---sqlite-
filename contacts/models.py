from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    avatar = models.ImageField(null=True, blank=True, upload_to='contact')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    birthdate = models.DateField(null=True, blank=True)

    phone_validator = RegexValidator(
        regex=r'^\d{8,12}$',
        message="El número de teléfono debe contener solo dígitos, entre 8 y 12 caracteres (ej: 56912345678)."
    )
    phone = models.CharField(validators=[phone_validator], null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True) # Se crea fecha de forma automatica

    def __str__(self) -> str:
        return self.name