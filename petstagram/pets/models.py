from django.db import models


# Create your models here.
from accounts.models import UserProfile
from functions.clean_up import clean_up_files


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    RABBIT = 'rabbit'
    UNKNOWN = 'unknown'
    PET_TYPES = [
        [DOG, 'Dog'],
        [CAT, 'Cat'],
        [PARROT, 'Parrot'],
        [RABBIT, 'Rabbit'],
        [UNKNOWN, 'Unknown'],

    ]

    type = models.CharField(max_length=50, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=15, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.ImageField(upload_to='images')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id}, NAME: {self.name}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id}, NAME: {self.pet.name}'


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

