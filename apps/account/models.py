from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=120)
    bank = models.CharField(max_length=70)
    credit = models.IntegerField()

    class Meta:
        ordering = ('name',)