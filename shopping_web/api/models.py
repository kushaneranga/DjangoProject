from django.db import models

# Create your models here.

class TypesCode(models.Model):
    name = models.CharField(max_length=100)
    oldprice = models.TextField()
    newprice = models.TextField()
    img = models.ImageField(upload_to='img/png')
    sale = models.BooleanField(default=False)
   