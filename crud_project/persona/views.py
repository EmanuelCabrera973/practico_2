from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Persona

class PersonaListView(LoginRequireMixin, ListView):
    model = Persona
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            return queryset.filter(nombre__icontains=search_query)
        return queryset
    
class PersonaCreateView(LoginRequiredMixin, CreateView):
    model = Persona
    fields = ['apellido', 'nombre', 'edad', 'oficina']
    succes_url = reverse_lazy('persona:lista')

class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    model = Persona
    fields = ['apellido', 'nombre', 'edad', 'oficina']
    sicces_url = reverse_lazy('persona:lista')
    
class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    model = Persona
    succes_url = reverse_lazy('persona:lista')
    
class PersonaDetailView(LoginRequiredMixin, DetailView):
    model = Persona
    


# Create your views here.
