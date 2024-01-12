from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.shortcuts import render, redirect

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

def book_detail(request, id:str):
    try:
        if (not Book.objects.filter(id=int(id)).exists()):
            messages.error(request, "View don't exists!")
            return redirect("booksSite")
        book = Book.objects.get(id=int(id))
        context = {
            'book': book
        }
        return render(request, 'view/book_view.html', context=context)
    except Exception as e:
        messages.error(request, e.__str__())
        return redirect("authorsSite")

def category_detail(request, id:str):
    try:
        if (not Category.objects.filter(id=int(id)).exists()):
            messages.error(request, "View don't exists!")
            return redirect("categorysSite")
        book = Category.objects.get(id=int(id))
        context = {
            'book': book
        }
        return render(request, 'view/category_view.html', context=context)
    except Exception as e:
        messages.error(request, e.__str__())
        return redirect("authorsSite")


def author_detail(request, id:str):
    try:
        if (not Author.objects.filter(id=int(id)).exists()):
            messages.error(request, "View don't exists!")
            return redirect("authorsSite")
        book = Author.objects.get(id=int(id))
        context = {
            'book': book
        }
        return render(request, 'view/author_view.html', context=context)
    except Exception as e:
        messages.error(request, e.__str__())
        return redirect("authorsSite")

def register(request):
   if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(username = username, password = password)
           login(request, user)
           return redirect('home')
   else:
       form = UserCreationForm()
   return render(request,'register.html', {'form': form})


def passwordReset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if (form.is_valid()):
            print("Nie wiem")
            return redirect('home')
    else:
        form = PasswordResetForm()
    return render(request, 'passwordReset.html', {'form': form})

def passwordChange(request):
    if request.method == 'POST':
        if (not request.user.is_authenticated): return redirect("login")
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("home")
    else:
        if request.user.is_authenticated:
            form = PasswordChangeForm(user=request.user)
        else:
            return redirect('login')
    return render(request, 'passwordChange.html', {'form': form})
