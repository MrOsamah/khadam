from django.urls import path
from . import views

urlpatterns = [
    path('' , views.MainPage),
    path('MedicalServices/' , views.MedicalServicesView),
    path('Lost/Report/' , views.LostViews),
    path('Lost/Find/' , views.LostViews2),
    path('Lost/' , views.LostV),
    path('uploads/' , views.LostViews2),
    path('Lost/Find/lostinfo/<int:moha>' , views.LostInfo  , name="item"),

]
