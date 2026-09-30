from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('Floral', 'Floral'),
        ('Woody', 'Woody'),
        ('Citrus', 'Citrus'),
        ('Fresh', 'Fresh'),
        ('Oriental', 'Oriental'),
        ('Unisex', 'Unisex'),
    ]

    name = models.CharField(max_length=200)

    brand = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount = models.PositiveIntegerField(default=0)

    description = models.TextField()

    fragrance_notes = models.CharField(
        max_length=300,
        help_text="Example: Rose, Vanilla, Musk"
    )

    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(
        upload_to='products/'
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name