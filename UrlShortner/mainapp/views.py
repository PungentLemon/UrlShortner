from django.shortcuts import render, redirect
from .models import Short_urls
from .forms import UrlForm
from .shortner import Shortner

# Create your views here.
def home(request,token):
    long_url = Short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit = False)
            a = Shortner().issure_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a= "Invalid URL"
    return render(request,'home.html', {'form':form,'a':a})