from django.db import models
import os

# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class User(models.Model):
    UserName = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Position = models.CharField(max_length=10)
    email = models.EmailField(max_length=70)
    Bio_description = models.TextField()
    Profile_Pic = models.FileField()

    def __str__(self):
        return self.FirstName + ' ' + self.LastName


class Workout(models.Model):
    Workout_Name = models.CharField(max_length=100)
    Workout_Description = models.TextField()
    likes = models.IntegerField(default=0)
    Position = models.CharField(max_length=10)

    def __str__(self):
        return self.Workout_Name


class Workout_Summary(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)
    Shots_Made = models.IntegerField()
    Shots_Attempted = models.IntegerField()

    def __str__(self):
        return "In the workout: {}, you went {}/{}".format(self.Workout, self.Shots_Made, self.Shots_Attempted)
