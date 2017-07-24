import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models



class Menu(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=200)
    available = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.name)


class MenuItem(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=200)
    cost = models.DecimalField(decimal_places=2, max_digits=5)
    available = models.BooleanField(default=False)
    menu = models.ForeignKey(Menu)

    def __str__(self):
        return '%s' % (self.name)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    MenuItem = models.ForeignKey(MenuItem)
    time = models.TimeField(blank=True, null=True)
    operator = models.ForeignKey(User, related_name='User', null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)