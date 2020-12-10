import os
from django.db import models
from users.models import UserModel


# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)
    price = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=50)
    sold_out = models.BooleanField(default=False)
    likes = models.IntegerField(default=0, blank=True)
    photos = models.ImageField(upload_to=os.path.join('Products', 'img'),
                               default='',
                               blank=True,
                               )
    user = models.ForeignKey(UserModel,
                             default='',
                             on_delete=models.SET_DEFAULT,
                             blank=True,
                             related_name='product'
                             )
