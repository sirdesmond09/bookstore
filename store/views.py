from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, "index.html")

def store(request):
    count = Book.objects.all().count()
    context = {
        'count':count
    }
    request.session['location'] = "unknown"
    if request.user.is_authenticated():
        request.session['location'] = "Nigeria"

    return render(request, "store.html", context)
