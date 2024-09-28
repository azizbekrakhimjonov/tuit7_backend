from django.shortcuts import render
from django.views.generic import ListView
from .models import Universitet, Talaba, Bino

class UniversitetListView(ListView):
    model = Universitet
    template_name = 'universitet_list.html'
    context_object_name = 'universitetlar'

class TalabaListView(ListView):
    model = Talaba
    template_name = 'talaba_list.html'
    context_object_name = 'talabalar'


class BinoListView(ListView):
    model = Bino
    template_name = 'bino_list.html'
    context_object_name = 'binolar'


