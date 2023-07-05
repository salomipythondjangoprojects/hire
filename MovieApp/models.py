from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()


class movies(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_desc = models.TextField()
    movie_img = models.ImageField(upload_to='moviepics')
    movie_trailor = models.FileField(upload_to='movievideo')


class show(models.Model):
    movie = models.ForeignKey(movies,on_delete=models.CASCADE)
    Timing = models.CharField(max_length=50)
    seats = models.IntegerField(default=50)

class employee(models.Model):
    employeeName = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    profilePic = models.ImageField(upload_to='employeePIC')
    employeeEmail = models.EmailField(null=True)

class messages(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)