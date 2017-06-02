from django.shortcuts import render , HttpResponse

# Create your views here.

def login(request) :
    name = 'Piyush'
    numbers = [1,2,3,4,5]
    arg = {'name':name, 'numbers':numbers }
    return render(request, 'login/login.html',arg)

def home(request):

    return render(request , 'home/home.html')

def index(request):
    return render(request , 'index/index.html')
