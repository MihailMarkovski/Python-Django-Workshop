from django.db import models


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    budget = models.IntegerField()

    def __str__(self):
        return f'First Name: {self.first_name} Last Name: {self.last_name} Budget: {self.budget}'


class Expense(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()


    def __str__(self):
        return f'Title: {self.title} Image: {self.image_url} Description: {self.description} Price: {self.price}'



