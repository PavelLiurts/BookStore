from django.forms import ModelForm
from refers.models import Author, Serie, Genre

class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]

class AuthorDeleteForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]

class AuthorUpdateForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]


class SerieCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]


class SerieDeleteForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]


class SerieUpdateForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]


class GenreCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]


class GenreDeleteForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]


class GenreUpdateForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]