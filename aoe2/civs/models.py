from django.db import models

# Create your models here.
class Civ(models.Model):
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    expansion = models.TextField()
    army_type = models.TextField()
    unique_unit = models.ManyToManyField(to='self')
    unique_tech = models.ManyToManyField(to='self')
    team_bonus = models.TextField()
    civilization_bonus = models.ManyToManyField(to='self')
