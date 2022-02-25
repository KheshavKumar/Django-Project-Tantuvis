from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_views(request,*args,**kwargs):#request is one of the args we have to explicitly call for certain functs
    print(request.user)
    return render(request, 'home.html',{})

   

def contact_views(request, *args, **kwargs):
    return render(request,'contact.html', {})

def about_views(request,*args, **kwargs):
    about_context={'my_name':'Kheshav',
    'my_no':911,
    'my_list':['a','b','c',123],
    }
    return render(request,'about.html', about_context)

def result_views(request,*args,**kwargs):
    a=int(request.POST['a'])
    b=int(request.POST['b'])
    #print(type(a))
    res=a+b
    #res=1+2
    return render(request,'result.html',{'result':res})