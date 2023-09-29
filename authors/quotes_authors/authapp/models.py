from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    fullname = models.CharField(null=False)
    born_date = models.CharField(default="01/01/1900")
    born_location = models.CharField(null=False)
    description = models.CharField(null=False)

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    quote = models.CharField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.CharField(null=True)

    def __str__(self):
        return f"{self.quote}"
