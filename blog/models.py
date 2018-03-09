from django.db import models


# Create your models here.
from django.shortcuts import redirect


class Blog(models.Model):
    judul = models.CharField(max_length=120)
    konten = models.TextField(max_length=1200)

    def get_absolute_url(self):
        return redirect('blog:index')
