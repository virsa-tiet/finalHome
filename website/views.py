from django.shortcuts import render
from website.models import contact 
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        msg=request.POST['msg']
        email=request.POST['email']
        print(name)
        data=contact.objects.create(
        name=name,
        msg=msg,
        email=email
        )
        data.save()
        return render(request,'home.html')
    return render(request,'home.html')
    
def Home(request):
    if request.method=='POST':
        name=request.POST['name']
        msg=request.POST['msg']
        email=request.POST['email']
        print(name)
        data=contact.objects.create(
        name=name,
        msg=msg,
        email=email
        )
        data.save()
        dic={'s': True}
        return render(request,'home.html',context=dic)
    return render(request,'home.html')

def pre_events(request):
    return render(request,'pre.html')

def main_events(request):
    return render(request,'main.html')

def online_events(request):
    return render(request,'online.html')

def core(request):
    return render(request,'core.html')

def heads(request):
    return render(request,'heads.html')

def gallery(request):
    return render(request,'gallery.html')

