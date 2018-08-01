from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.MainPage),
    path('MedicalServices/' , views.MedicalServicesView),
    path('Lost/' , views.LostViews),
]
