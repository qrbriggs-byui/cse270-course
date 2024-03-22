from django.db import models

# Create your models here.
class Principal(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    user_role = models.CharField(max_length=50)

    def __str__(self):
        return self.username