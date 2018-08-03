from django.shortcuts import render , redirect
from .forms import MedicalServicesForm , LostForm
from .models import Lost3

def MainPage(request):
    return render(request , 'MainPage.html')

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

def LostViews2(request):
    items = Lost3.objects.all()
    args = {'items' : items}
    return render(request , 'LostFind.html' , args )

def LostV(request):
    return render(request , 'LostMain.html')

def LostInfo(request , moha):
    items = Lost3.objects.get(pk=moha)
    args = {'items': items}
    return render(request , 'LostInfo.html' , args)
