from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=30)
    msg=models.TextField(max_length=300)
    email=models.EmailField(blank=False)
    