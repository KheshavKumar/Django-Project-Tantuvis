from django.shortcuts import render
from .models import destination

def index_views(request):
   dests = destination.objects.all()
  
   """
   dest1=destination()
   dest1.name='Mumbai'
   dest1.desc='City that never sleeps'
   dest1.price=420
   dest1.img='destination_1.jpg'
   dest1.offer=True

   dest2=destination()
   dest2.name='Hyderabad'
   dest2.desc='Spicy Biriyani'
   dest2.price=500
   dest2.img='destination_2.jpg'
   dest2.offer=False

   dest3=destination()
   dest3.name='Bengaluru'
   dest3.desc='I Live Here'
   dest3.price=600
   dest3.img='destination_3.jpg'
   dest3.offer=False

   dests=[dest1,dest2,dest3]"""
   return render(request,'index.html',{'dests':dests})

def about_views(request):
   return render(request,'about.html',{})
