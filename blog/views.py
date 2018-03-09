from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView
from .models import *
from django.views.generic.base import View


class Index(ListView):
    model = Blog
    template_name = 'blog/index.html'


class Tambah(CreateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/tambah.html'


class Detail(DetailView):
    model = Blog
    template_name = 'blog/singel.html'
