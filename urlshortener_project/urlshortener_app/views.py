import string
import random
from django.shortcuts import render, redirect
from .models import URL

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        url, created = URL.objects.get_or_create(original_url=original_url)
        return render(request, 'shortener/shorten.html', {'short_url': url.short_code})
    return render(request, 'shortener/shorten.html')

def redirect_url(request, short_code):
    try:
        url = URL.objects.get(short_code=short_code)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return render(request, 'shortener/404.html')
