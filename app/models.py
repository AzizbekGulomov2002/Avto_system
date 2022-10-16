from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    nomi = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='avto_kategoriyalar/', null=True, blank=True)

    def __str__(self):
        return self.nomi


    class Meta:
            verbose_name = 'Kategoriya'
            verbose_name_plural = 'Kategoriyalar'


class Avtomobil(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=200)
    yil = models.IntegerField()
    rasm = models.ImageField(upload_to='avto_rasmlar/')
    manzil =  models.CharField(max_length=200)
    probeg = models.IntegerField()
    kuzov = models.CharField(max_length=200)
    dvigatel = models.CharField(max_length=200)
    rang = models.CharField(max_length=200)
    narx = models.CharField(max_length=200,help_text="So'z ko'rinishida ham yozish mumkin...")
    tel_nomer = models.IntegerField()
    egasi = models.CharField(max_length=200)
    yuklangan_sana = models.DateTimeField(auto_now_add=True)
    xarakteristika = models.TextField()

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillar'





