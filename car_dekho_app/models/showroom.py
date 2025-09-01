from django.db import models

class Showrooms(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    website = models.URLField(max_length=200, blank=True, null=True)
    # cars = models.ManyToManyField(models.Cars, related_name='showrooms')

    def __str__(self):
        return self.name