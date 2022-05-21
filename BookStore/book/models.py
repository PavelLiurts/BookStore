from django.db import models
from refers.models import Author,Serie,Genre

class Book(models.Model):
    title = models.CharField(max_length=100,blank=False, null=False)
    description = models.CharField(max_length=500,blank=True)
    cover = models.ImageField(upload_to='', blank=True)
    isbn = models.CharField(max_length=100, blank=True)
    author = models.ManyToManyField(
        Author,
    )
    serie = models.ForeignKey(
        Serie,
        on_delete=models.PROTECT
    )
    genre = models.ManyToManyField(
        Genre,
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cataloging = models.DateField(auto_now_add=True)
    last_change = models.DateField(auto_now=True)
    available_order = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "Book"
        verbose_name_plural = "Books"

    def get_absolute_url(self):
        return '/books/{self.pk}'

