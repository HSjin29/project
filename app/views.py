from django.shortcuts import render
from django.http import HttpResponse
from .models import Login, USER
from django.views.decorators.csrf import csrf_exempt



    
def mapp(request):
    return render(request, 'map.html')

def index(request):
    return render(request, 'index.html')

def log(request):
    return render(request, '로그인.html')

def pick(request):
    return render(request, '업로드.html')


def login(request):
    if request.method == 'POST':
        log_id= request.POST.get('log_id')
        log_password= request.POST.get('log_password')

        c=Login(log_id=log_id, log_password=log_password)
        c.save()

        return render(request, '이벤트.html')
    return render(request, 'login.html')


def user(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        job=request.POST.get('job')
        city=request.POST.get('city')
        add=request.POST.get('add')

        c= USER(id=id, name=name, age=age, email=email, phone=phone, job=job, city=city, add=add)
        c.save()

        return render(request,'이벤트.html')
    return render(request, 'signup.html')
