from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class Serie(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name