from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
    
def Home(request):
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