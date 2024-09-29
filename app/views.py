from django.shortcuts import render
from django.views.generic import ListView
from .models import Universitet, Bino

class UniversitetListView(ListView):
    model = Universitet
    template_name = 'universitet_list.html'
    context_object_name = 'universitetlar'


class BinoListView(ListView):
    model = Bino
    template_name = 'bino_list.html'
    context_object_name = 'binolar'


