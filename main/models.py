from django.db import models
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator, 
    URLValidator,
    validate_slug
)
from main.validators import validate_even_number

# Create your models here.
# every table in the database is represented as class
# every row in database is represented by object of this class
class Student(models.Model):
    GENDERS = (
        ('f', 'Female'), 
        ('m', 'male'),
        ('u', 'Undisclosed')
    )

    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    address = models.TextField(null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(null=True,max_length=100, validators=[EmailValidator("Email address is not valid")])  #varchar(255) 
    gender = models.CharField(max_length=1, choices=GENDERS, null=True)
    age = models.IntegerField(
        null=True,
        validators= [
        MaxValueValidator(150), 
        MinValueValidator(0), 
        validate_even_number,
         ]      
     )
    
    slug = models.CharField(max_length= 100, validators=[validate_slug], null=True)


    def __str__(self):
        return self.name