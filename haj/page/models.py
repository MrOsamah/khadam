from django.db import models

class MedicalServices(models.Model):
    Service_Name = models.CharField(max_length=140)
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
    Location = models.ForeignKey(MedicalServices , on_delete="CASCAD")
    Gender = models.CharField(max_length=1 , choices=Gender_choices , default="")
    Nationality = models.CharField(max_length=2 , choices=Nationality_choices , default="")
    Photo = models.FileField(upload_to='uploads/')
