from django.db import models
from django.contrib.auth.models import User
# Create your models here.

DIVISION_CHOICES = (
    ('','Choose Your Divicion'),
    ('Dhaka', 'Dhaka'),
    ('Khulna', 'Khulna'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Rajshahi', 'Rajshahi'),
    ('Barishal', 'Barishal'),
    ('Chattogram', 'Chattogram'),
    ('Mymendhing', 'Mymendhing'),
) 


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    name = models.CharField(max_length=150),
    institution = models.CharField(max_length=150),
    division = models.CharField(choices=DIVISION_CHOICES ,max_length=50),
    district = models.CharField(max_length=50),
    Thana = models.CharField(max_length=50),
    zipcode = models.IntegerField(),
    image = models.ImageField(),
    
    
    def __str__(self):
        return str(self.id)
    
    