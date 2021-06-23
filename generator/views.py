from django.shortcuts import render
#render allows to passback a template to the HttpResponse
from django.http import HttpResponse
#the key should be a string while declaring in the render
# Create your views here.
import random

def home(request):
    return render(request,'generator/home.html')
def password(request):

    thepass = ""
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special characters'):
        characters.extend(list('@#$%^&*()+_|!~'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    length = int(request.GET.get('length',12))
    for x in range(length):
        thepass += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepass})

def about(request):
    return render(request,'generator/about.html')
