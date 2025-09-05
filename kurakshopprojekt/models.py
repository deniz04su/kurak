# kurakshopprojekt/models.py
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Аты')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категориялар'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Аталышы")
    description = models.TextField(blank=True, null=True, verbose_name="Сүрөттөмө")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баасы")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория", null=True, blank=True)
    available = models.BooleanField(default=True, verbose_name="Барбы?")
    is_original = models.BooleanField(default=True, verbose_name="Оригиналбы?")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон номер")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Сүрөтү")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Кошулган убак")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Жаңыртылган убак")

    class Meta:
        verbose_name = "Продукция"
        verbose_name_plural = "Продукциялар"

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(15), MaxValueValidator(75)],
        null=True, blank=True
    )
    STATUS_CHOICES = (
        ('gold','gold'),
        ('silver','silver'),
        ('bronze','bronze'),
        ('simple','simple')
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='simple')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} → {self.receiver}: {self.message[:20]}"
