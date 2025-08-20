from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Oficina

class OficinaListView(LoginRequiredMixin,ListView):
    model=Oficina
    paginate_by=10

class OficinaCreateView(LoginRequiredMixin, CreateView):
    model=Oficina
    fields = ['nombre', 'nombre_corto']
    succes_url = reverse_lazy('oficina:lista')
    
class OficinaUpdateView(LoginRequiredMixin, UpdateView):
    model=Oficina
    fields= ['nombre', 'nombre_corto']
    succes_url = reverse_lazy('oficina:lista')
    
class OficinaDeleteView(LoginRequiredMixin, DeleteView):
    model = Oficina
    succes_url = reverse_lazy('oficina:lista')
    
class OficinaDeltailView(LoginRequiredMixin, DetailView):
    model = Oficina
    

# Create your views here.
