from django.db import models

# Universitet ma'lumotlari modeli
class Universitet(models.Model):
    nomi = models.CharField(max_length=255)  # Universitet nomi
    manzil = models.CharField(max_length=255)  # Universitet manzili
    asos_sanasi = models.DateField()  # Universitet tashkil topgan sana
    rektor = models.CharField(max_length=100)  # Rektor ismi

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

# Talaba ma'lumotlari modeli
class Talaba(models.Model):
    talaba_id = models.CharField(max_length=50)  # Talabaning idsi
    ism = models.CharField(max_length=50)  # Talabaning ismi
    familiya = models.CharField(max_length=50)  # Talabaning familiyasi
    tugilgan_sana = models.DateField()  # Tug'ilgan sana
    fakultet = models.CharField(max_length=100)  # Fakultet nomi
    kurs = models.PositiveIntegerField()  # Talabaning kursi
    bino = models.ForeignKey(Bino, on_delete=models.CASCADE)  # Talaba o'qiydigan bino

    def __str__(self):
        return f'{self.ism} {self.familiya}'
