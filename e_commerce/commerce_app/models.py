from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)# 100 karaktere kadar ürün adı saklar.
    product_price = models.DecimalField(max_digits=10,decimal_places=2)# burada virgülden sonra 10 basamklı sayı saklar. Virgülden önce iki basamağa dek izin verir.
    description = models.TextField()# ürün  açıklaması için metin saklar.
    image_url = models.URLField()# ürün resmi için url saklar.
    
    def __str__(self):
        return self.product_name  # Ürün adını string olarak döndürür.
    # __str__ metodu, modelin string temsili için kullanılır.

class Users(models.Model):
    username = models.CharField(max_length = 100) #kullanıcı adı alınır.
    surname = models.CharField(max_length=100) # soyad alınır
    password = models.BinaryField(max_length=8)# 8 byte uzunluğunda ikili veri saklar.
    e_mail = models.EmailField(max_length=200, ) # e-posta adresi alınır.
    