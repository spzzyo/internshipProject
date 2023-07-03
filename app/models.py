from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        ('1', 'Admin'),
        ('2', 'Instructor'),
    )

    user_type = models.CharField(choices=USER, max_length=60,default='1')






class Instructor(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username


class Course(models.Model):

    LEVEL_CHOICES = [
        ("1", 'Level 1'),
        ("2", 'Level 2'),
        ("3", 'Level 3'),
        ("4", 'Level 4'),
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20,choices=LEVEL_CHOICES, default="1")
    description = models.TextField()
    image = models.ImageField(upload_to='media/coursePicture', default='media/coursePicture/default.png')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
class Lectures(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete= models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
   
