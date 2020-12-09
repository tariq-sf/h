from django.shortcuts import render

from .models import home


# Create your views here.

def home_list(request):
    home_list=home.objects.all()
    
    context={'homes':home_list}
    return render(request,'home/home_list.html',context)

def home_detail(request):
    return HttpResponse('delait view')
