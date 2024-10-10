from django.shortcuts import render,HttpResponse,redirect
from .models import UserData
from django.contrib.auth import authenticate,login

def index(request):
    return HttpResponse("hello ji jai shree ram")

def home_view(request):
    return render(request,'ecomm/home.html')

def register_view(request):
    if request.method=='POST':
        first_name= request.POST.get('fname')
        last_name= request.POST.get('lname')
        email= request.POST.get('email')
        password= request.POST.get('password')

        user = UserData.objects.create(first_name= first_name, last_name= last_name, email=email,password=password)
        user.save()
    return render(request, 'ecomm/register.html')

def login_view(request):
    if request.method== 'POST':
        email= request.POST.get('email')
        password= request.POST.get('password')

        try:
            user= UserData.objects.get(email=email, password=password)

            if user:
                request.session['user_id']= user.id
                return redirect('index')
        except:
            return render(request, 'ecomm/login.html', {'error': 'Invalid email or password'})
    return render(request, 'ecomm/login.html')