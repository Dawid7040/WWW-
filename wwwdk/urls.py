"""
URL configuration for wwwdk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from LessonsWWW import views
from LessonsWWW.views import register, passwordReset, passwordChange

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_render, name='home'),
    path('books/', views.books_list, name='booksSite'),
    path('author/', views.authors_list, name="authorsSite"),
    path('categorys/', views.categorys_list, name="categorysSite"),
    path('book/view/<str:id>',views.book_detail, name="bookView" ),
    path('author/view/<str:id>',views.author_detail, name="authorView" ),
    path('category/view/<str:id>',views.category_detail, name="categoryView" ),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password/reset/', passwordReset, name='passwordReset' ),
    path('password/change/', passwordChange, name='passwordChange' )
]
