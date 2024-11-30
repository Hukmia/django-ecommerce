from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser): 
    is_admin = models.BooleanField('is admin', default=False)
    is_staff = models.BooleanField('is staff', default=False)
    is_pelanggan = models.BooleanField('is pelanggan', default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)

    gender = models.CharField(max_length=10, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], blank=True, null=True)
    agama = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
