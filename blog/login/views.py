from django.shortcuts import render , HttpResponse

# Create your views here.

def home(request) :
    name = 'Piyush'
    arg = {'name':name}
    return render(request, 'login/login.html',arg)
