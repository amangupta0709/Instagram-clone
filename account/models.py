from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=140)

    def __str__(self):
        return self.username
