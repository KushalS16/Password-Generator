import random
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    Characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        Characters.extend(list('0123456789'))
    if request.GET.get('Special'):
        Characters.extend(list('!@#$%^&*()-=_+'))
    length=int(request.GET.get('length',8))

    thepassword=''
    for i in range(length):
        thepassword += random.choice(Characters)

    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')




    


