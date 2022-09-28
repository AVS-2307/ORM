from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    release_date = models.DateField(auto_now_add=True)
    lte_exists=models.BooleanField(default=True)
    slug = models.SlugField(max_length=100)