from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models

class PlantListView(ListView):
    model = models.Plant
    template_name = 'plant_list.html'

class PlantCreateView(CreateView):
    model = models.Plant
    template_name = 'plant_new.html'
    fields = ['common_name', 'species_name', 'genus']

class PlantDetailView(DetailView):
    model = models.Plant
    template_name = 'plant_detail.html'

class PlantUpdateView(UpdateView):
    model = models.Plant
    fields = ['common_name', 'species_name']
    template_name = 'plant_edit.html'

class PlantDeleteView(DeleteView):
    model = models.Plant
    template_name = 'plant_delete.html'
    success_url = reverse_lazy('plant_list')
