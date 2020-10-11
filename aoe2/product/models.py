from django.db import models

# Create your models here.
class Product(models.Model):
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types
    title = models.CharField(max_length=120) #max_length = Required
    description = models.TextField()
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    # blank is required or not
    # null is empty in the database or not
    summary = models.TextField(blank=False, null=False)
    features = models.BooleanField(default=False)