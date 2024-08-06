from django.http import HttpResponse
from django.shortcuts import render
from Art_gallery.models import Artgallery
from Bridal_gallery.models import Bridalgallery
from Party_look_gallery.models import Partylookgallery
from Mehndi_gallery.models import Mehndigallery
from User_info.models import User_info

def aboutus(request):
    return HttpResponse("Hey there")

# def send(request):
#     if request.method == 'POST':
#         Name=request.POST.get("name")
#         Email=request.POST.get("email")
#         Phone=request.POST.get("phone")
#         Date=request.POST.get("date")
#         print(Name+' '+Email+' '+Phone+' '+Date)
#         data=User_info(name=Name,email=Email,phone=Phone,date=Date)
#         data.save()
#     return render(request,'index.html')


def home(request):
    try:
        if request.method == 'POST':
            print('HELLO')
            Name=request.POST.get("name")
            Email=request.POST.get("email")
            Phone=request.POST.get("phone")
            Date=request.POST.get("date")
            print(Name,Email,Phone,Date)
            data=User_info(name=Name,email=Email,phone=Phone,date=Date)
            data.save()
    except:
        pass
    return render(request,'index.html')

def artgallery(request):
    try:
        if request.method == 'POST':
            print('HELLO')
            Name=request.POST.get("name")
            Email=request.POST.get("email")
            Phone=request.POST.get("phone")
            Date=request.POST.get("date")
            print(Name,Email,Phone,Date)
            data=User_info(name=Name,email=Email,phone=Phone,date=Date)
            data.save()
    except:
        pass
    data = Artgallery.objects.all()
    x=[]
    for i in data:
        x.append(i.photo)
    y=[]
    z=[]
    c=0
    for i in x:
        y.append(i)
        c=c+1
        if c==2:
            z.append(y)
            y=[]
            c=0
    x=z.copy()
    return render(request,'art_gallery.html',{'Data':x})

def bridalgallery(request):
    try:
        if request.method == 'POST':
            print('HELLO')
            Name=request.POST.get("name")
            Email=request.POST.get("email")
            Phone=request.POST.get("phone")
            Date=request.POST.get("date")
            print(Name,Email,Phone,Date)
            data=User_info(name=Name,email=Email,phone=Phone,date=Date)
            data.save()
    except:
        pass
    data = Bridalgallery.objects.all()
    x=[]
    for i in data:
        x.append(i.photo)
    y=[]
    z=[]
    c=0
    for i in x:
        y.append(i)
        c=c+1
        if c==2:
            z.append(y)
            y=[]
            c=0
    x=z.copy()
    return render(request,'bridal_gallery.html',{'Data':x})


def partylookgallery(request):
    try:
        if request.method == 'POST':
            print('HELLO')
            Name=request.POST.get("name")
            Email=request.POST.get("email")
            Phone=request.POST.get("phone")
            Date=request.POST.get("date")
            print(Name,Email,Phone,Date)
            data=User_info(name=Name,email=Email,phone=Phone,date=Date)
            data.save()
    except:
        pass
    data = Partylookgallery.objects.all()
    x=[]
    for i in data:
        x.append(i.photo)
    y=[]
    z=[]
    c=0
    for i in x:
        y.append(i)
        c=c+1
        if c==2:
            z.append(y)
            y=[]
            c=0
    x=z.copy()
    return render(request,'party_look_gallery.html',{'Data':x})

def mahndigallery(request):
    try:
        if request.method == 'POST':
            print('HELLO')
            Name=request.POST.get("name")
            Email=request.POST.get("email")
            Phone=request.POST.get("phone")
            Date=request.POST.get("date")
            print(Name,Email,Phone,Date)
            data=User_info(name=Name,email=Email,phone=Phone,date=Date)
            data.save()
    except:
        pass
    data = Mehndigallery.objects.all()
    x=[]
    for i in data:
        x.append(i.photo)
    y=[]
    z=[]
    c=0
    for i in x:
        y.append(i)
        c=c+1
        if c==2:
            z.append(y)
            y=[]
            c=0
    x=z.copy()
    return render(request,'mehndi_gallery.html',{'Data':x})