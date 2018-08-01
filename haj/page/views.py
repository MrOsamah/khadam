from django.shortcuts import render , redirect , HttpResponseRedirect
from .forms import MedicalServicesForm , LostForm

def MainPage(request):
    return render(request , 'MainPage.html')

#----------------------------------


def MedicalServicesView(request):
    if request.method == 'POST':
        form = MedicalServicesForm(request.POST , request.FILES)
        Photo = request.POST.get('Photo')
        if form.is_valid():
            form.save()
            return redirect('/')
    else :
        form = MedicalServicesForm()
        args = {'form' : form}
        return render(request , 'MedicalServices.html' , args )


def LostViews(request):
    if request.method == 'POST':
        form = LostForm(request.POST , request.FILES)
        Photo = request.POST.get('Photo')
        if form.is_valid():
            form.save()
            return redirect('/')
    else :
        form = LostForm()
        args = {'form' : form}
        return render(request , 'Lost.html' , args )
