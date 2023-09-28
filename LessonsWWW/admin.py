from django.contrib import admin

from LessonsWWW.models import Author, Category, Book

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "year_of_birth"]
    list_filter = ["year_of_birth", "last_name"]
    search_fields = ["first_name", "last_name"]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["category_name"]

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "description"]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)