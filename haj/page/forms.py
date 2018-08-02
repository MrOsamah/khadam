from django import forms
from . import models

class MedicalServicesForm(forms.ModelForm):
    class Meta:
        model = models.MedicalServices
        fields = ('Name' , 'Nationality' , 'Gender'  , 'Age' , 'Injury' , 'Description')



class LostForm(forms.ModelForm):
    class Meta:
        model = models.Lost
        fields = ( 'Name' ,'Nationality' , 'Gender' , 'Age' ,'Photo' )
