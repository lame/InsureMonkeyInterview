from django.db import models


class User(models.Model):
    user = models.CharField(max_length=20)


class Address(models.Model):
    user = models.ForeignKey('User')
    address = models.CharField(max_length=80)
