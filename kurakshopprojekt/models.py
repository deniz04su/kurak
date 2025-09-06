from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

# ----------------------
# Кастомный пользователь
# ----------------------
class User(AbstractUser):
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(15), MaxValueValidator(75)],
        null=True, blank=True
    )
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('simple', 'simple')
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='simple')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# ----------------------
# Профиль пользователя
# ----------------------
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="profiles/", default="profiles/default.jpg")

    def __str__(self):
        return self.user.username


# ----------------------
# Категории
# ----------------------
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


# ----------------------
# Продукты
# ----------------------
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория", null=True, blank=True)
    available = models.BooleanField(default=True, verbose_name="В наличии?")
    is_original = models.BooleanField(default=True, verbose_name="Оригинал?")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


# ----------------------
# Медиа для продуктов
# ----------------------
class ProductMedia(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media', verbose_name="Продукт")
    image = models.ImageField(upload_to='product_media/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Медиа продукта"
        verbose_name_plural = "Медиа продуктов"

    def __str__(self):
        return f"Media для {self.product.name}"


# ----------------------
# Чат-сообщения
# ----------------------
class ChatMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} → {self.receiver}: {self.message[:20]}"


# ----------------------
# Комментарии к продуктам
# ----------------------
class ProductComment(models.Model):
    product = models.ForeignKey('kurakshopprojekt.Product', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product}"


# ----------------------
# Реакции на продукты
# ----------------------
class ProductReaction(models.Model):
    product = models.ForeignKey('kurakshopprojekt.Product', on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=20, choices=[('like','Like'),('dislike','Dislike')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} reacted {self.reaction_type} to {self.product}"


# ----------------------
# Статус продуктов
# ----------------------
class ProductStatus(models.Model):
    product = models.ForeignKey('kurakshopprojekt.Product', on_delete=models.CASCADE, related_name='statuses')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_statuses', blank=True)
    status_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Status by {self.user} on {self.product}"
