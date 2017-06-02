from django.shortcuts import render , HttpResponse

# Create your views here.

def home(request) :
    name = 'Piyush'
    numbers = [1,2,3,4,5]
    arg = {'name':name, 'numbers':numbers }
    return render(request, 'login/login.html',arg)
