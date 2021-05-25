from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'doaksodko'})
def Autor(request):
    return render(request, 'generator/Autor.html')
def password(request):


    caratteri=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        caratteri.extend(list('ABCDEFGHIJKLMNOPQRSTIVWXYZ'))
    if request.GET.get('numeri'):
        caratteri.extend(list('1234567890'))
    if request.GET.get('caratteri speciali'):
        caratteri.extend(list('.,;_-*+@&%!°#?'))
    lenght=int(request.GET.get('lenght',12))
    password=''

    for z in range(lenght):
        password+=random.choice(caratteri)




    return render(request, 'generator/password.html',{'password':password})
