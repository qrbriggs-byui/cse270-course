from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    city_state_zip = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    website = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    membership_level = models.CharField(max_length=50)
    ad_copy = models.TextField()

    def __str__(self):
        return self.name