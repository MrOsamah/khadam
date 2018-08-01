from django import forms
from . import models

class MedicalServicesForm(forms.ModelForm):
    #Service_name = forms.CharField(max_length=140)
    #Description = forms.CharField(max_length=)
    class Meta:
        model = models.MedicalServices
        fields = ('Service_Name' , 'Description' , 'Photo' )



class LostForm(forms.ModelForm):
    class Meta:
        model = models.Lost
        fields = ( 'Name' ,'Gender' , 'Nationality' , 'Photo')
