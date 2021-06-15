from django.db import models


# Create your models here.



class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'
    PET_TYPES = [
        [DOG, 'Dog'],
        [CAT, 'Cat'],
        [PARROT, 'Parrot'],
        [UNKNOWN, 'Unknown'],

    ]

    type = models.CharField(max_length=50, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=15, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.URLField()

    def __str__(self):
        return f'ID: {self.id}, NAME: {self.name}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'ID: {self.id}, NAME: {self.pet.name}'


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)

