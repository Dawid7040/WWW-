from django.shortcuts import render

from LessonsWWW.models import Book, Author, Category


# Create your views here.
def home_render(request):
    context = {
        'message': 'Witaj na stronie głównej'
    }

    return render(request, "home.html", context=context)

def books_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, 'books-list.html', context=context)

def categorys_list(request):
    books = Category.objects.all()
    context = {"category": books}
    return render(request, 'categorys-list.html', context=context)

def authors_list(request):
    books = Author.objects.all()
    context = {"author": books}
    return render(request, 'authors-list.html', context=context)