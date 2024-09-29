from django.db import models

class Universitet(models.Model):
    nomi = models.CharField(max_length=255)
    manzil = models.CharField(max_length=255)
    asos_sanasi = models.DateField()
    rektor = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    xorij_hamkorlik = models.BooleanField(default=False)

    # Davlat yoki Nodavlat maydoni (BooleanField)
    davlat = models.BooleanField(default=True)  # True - davlat, False - nodavlat

    def __str__(self):
        return self.nomi


# Bino ma'lumotlari modeli
class Bino(models.Model):
    universitet = models.ForeignKey(Universitet, on_delete=models.CASCADE)  # Qaysi universitetga tegishli
    nomi = models.CharField(max_length=100)  # Bino nomi
    manzil = models.CharField(max_length=255)  # Bino manzili
    qavat_soni = models.PositiveIntegerField()  # Bino qavatlari soni
    sigimi = models.PositiveIntegerField()  # Bino sig'imi, talaba soni
    qurilish_yili = models.PositiveIntegerField()  # Qurilgan yili

    def __str__(self):
        return self.nomi

