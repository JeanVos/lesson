from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisements
from .forms import AdvertisementsForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    advertisement = Advertisements.objects.all()
    context = {'advertisements': advertisement}
    return render(request,'app_advertisements/index.html', context)

def top_sellers(request):
    return render(request, "app_advertisements/top-sellers.html")

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisements(**form.cleaned_data)
            advertisements.user = request.user
            advertisements.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form  = AdvertisementsForm()
    context ={"form": form}
    return render(request,'app_advertisements/advertisement-post.html',context)
