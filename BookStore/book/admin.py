from django.contrib import admin
from book.models import Book
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = (
            'id',
            'description',
            'price',
            'authors',
            'serie',
            'genres',
            'year_publishing',
            'pages',
            'binding',
            'format',
            'isbn',
            'weight',
            'age_restrictions',
            'publishing_house',
            'quantity',
            'rating',
            'cataloging',
            'last_change',
            'available_order'
        )

    class BookAdmin(ImportExportModelAdmin):
        resource_class = BookResource
