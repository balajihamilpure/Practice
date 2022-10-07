from django.db import models

# Create your models here.
class contact_us(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.BigIntegerField(max_length=10)
    message=models.TextField()