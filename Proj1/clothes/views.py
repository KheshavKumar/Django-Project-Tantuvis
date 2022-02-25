from django.shortcuts import render
from .models import Products

# Create your views here.
def home_views(request):
    all_items = Products.objects.all()
    return render(request,'homepage.html',{'all_items':all_items})
    #return render(request,'base.html',{})

def material_silk_views(request):
    all_items = Products.objects.all()
    return render(request,'Materials_Silk.html',{'all_items':all_items})

def material_cotton_views(request):
    all_items = Products.objects.all()
    return render(request,'Materials_Cotton.html',{'all_items':all_items})

def about_views(request):
    return render(request,'about.html')


    