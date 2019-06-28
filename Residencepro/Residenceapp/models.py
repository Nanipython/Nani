from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    password = models.IntegerField()
    confirm_password = models.IntegerField()

