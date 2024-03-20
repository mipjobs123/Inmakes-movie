from django.db import models
class Movie(models.Model): #Model is an inbuilt base class provided by Django for defining database models,
                           # It's part of the models module.

    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.name