from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=150)
    book_name = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='img', null=True, blank=True)
    description = models.CharField(max_length=450)

    def __str__(self):
        return self.book_name + "Uploaded by " + self.user.username
