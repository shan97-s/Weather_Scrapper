from django.db import models
from datetime import date
from django.contrib.auth.models import User
# # Create your models here.
class Records(models.Model):
    city = models.CharField(max_length=100)
    temp = models.TextField(max_length=100)
    description = models.TextField(max_length=250)
    time= models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})