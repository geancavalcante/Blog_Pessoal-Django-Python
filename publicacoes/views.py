from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import Books

def home(request):
    return render(request, 'index.html')

def publish(request):
    #posting = Posting.objects.all()
    return render(request, 'publish.html', {'posting': ''})

def sobre(request):
    return render (request, 'sobre.html')

def books(request):
    books = Books.objects.all()
    return render (request, 'books.html', {'books': books})

def form_posting(request):
    if request.method == "GET":
        return authentication(request)
    elif request.method == "POST": 
        title = request.POST.get('title')
        text_introdution = request.POST.get('text_introdution')
        text_development = request.POST.get('text_development')
        text_conclusion = request.POST.get('text_conclusion')
    
        return render(request, 'form_posting.html')

def form_book(request):
    if request.method == "GET":
        return render(request, 'form_book.html')
        
    elif request.method == "POST": 
        book = request.POST.get('book')
        link = request.POST.get('link')

        book = Books(book=book, link=link)
        book.save()
        
        return render(request, 'form_book.html')


def authentication(request):
    if request.method == "GET":
      return render(request, 'authentication.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name, password = password)
        if user:
            return render(request, 'form_posting.html')
        else:
            return render(request, 'authentication.html')
