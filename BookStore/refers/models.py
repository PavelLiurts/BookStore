from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/authors/{self.pk}'

class Serie(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Serie"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/series/{self.pk}'

class Genre(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/genres/{self.pk}'