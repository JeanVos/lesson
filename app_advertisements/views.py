from django.shortcuts import render
from .models import Advertisements
#from django.http import HttpResponse

def index(request):
    advertisement = Advertisements.objects.all()
    context = {'advertisements': advertisement}
    return render(request,'index.html', context)

def top_sellers(request):
    return render(request, "top-sellers.html")

# def advertisements_post(request):
#     return render(request,'advertisements-post.html')
