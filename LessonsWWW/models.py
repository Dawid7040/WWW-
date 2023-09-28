from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name_plural = 'Categories'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    description = models.CharField(max_length=213525, default='', blank=True)

    def __str__(self):
        return f'{self.title}, {self.author}, {self.category}, {self.description}'