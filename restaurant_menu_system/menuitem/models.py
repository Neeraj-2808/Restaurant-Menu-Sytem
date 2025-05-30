from django.db import models

import uuid

# Create your models here. 

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True



class Menuitems(BaseClass):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50)

    price = models.FloatField()

    menu = models.ForeignKey('menu.Menu',null=True,on_delete=models.SET_NULL)

    is_vegetarian =  models.BooleanField()



    def __str__(self):

        return f'{self.name}'
    

    class Meta:

        verbose_name = 'Menu'

        verbose_name_plural = 'Menus'

        ordering = ['-id']



