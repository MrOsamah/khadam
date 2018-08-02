from django.db import models

class MedicalServices(models.Model):
    Male= 'M'
    Female = 'F'
    Saudi = 'SA'
    Pakistani = 'PA'
    Iranian = 'IR'
    Gender_choices =  (
        ('M' , 'Male'),
        ('F' , 'Female')
    )
    Nationality_choices = (
        ('SA' , 'Saudi'),
        ('PA' , 'Pakistani'),
        ('IR' , 'Iranian')
    )
    Injury_choice = (
    ('H' , 'Head'),
    ('C' , 'Chest'),
    ('S' , 'Stomach'),
    ('D' , 'Hands'),
    ('L' , 'Legs')

    )
    Name = models.CharField(max_length=30)
    Gender = models.CharField(max_length=1 , choices=Gender_choices , default="")
    Nationality = models.CharField(max_length=2 , choices=Nationality_choices , default="")
    Age = models.IntegerField()
    Service_Name = models.CharField(max_length=140)
    Injury = models.CharField(max_length=1  , default=""  , choices=Injury_choice)
    Description = models.TextField(max_length=140)
    Photo = models.FileField(upload_to='uploads/')


class Lost(models.Model):
    Male= 'M'
    Female = 'F'
    Saudi = 'SA'
    Pakistani = 'PA'
    Iranian = 'IR'
    Gender_choices =  (
        ('M' , 'Male'),
        ('F' , 'Female')
    )
    Nationality_choices = (
        ('SA' , 'Saudi'),
        ('PA' , 'Pakistani'),
        ('IR' , 'Iranian')
    )
    
    Name = models.CharField(max_length=30)
    Gender = models.CharField(max_length=1 , choices=Gender_choices , default="")
    Nationality = models.CharField(max_length=2 , choices=Nationality_choices , default="")
    Age = models.IntegerField()
    Photo = models.FileField(upload_to='uploads/')
