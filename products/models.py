import os
from django.db import models
from users.models import UserModel


# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    price = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=50)
    sold_out = models.BooleanField(default=False)
    likes = models.IntegerField(default=0, blank=True)
    photos = models.FileField(blank=True, default='')
        # upload_to=os.path.join('Products', 'img'),
        #                       default='',
        #                       )
    user = models.ForeignKey(UserModel,
                             default='',
                             on_delete=models.SET_DEFAULT,
                             blank=True,
                             related_name='product'
                             )


class ProductImage(models.Model):
    product = models.ForeignKey(ProductModel, default='', on_delete=models.SET_DEFAULT)
    images = models.FileField(upload_to=os.path.join('Products', 'img'), default='', blank=True)
    default = models.BooleanField(default=False)
