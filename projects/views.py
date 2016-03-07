from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Project


class ProjectCreate(CreateView):
    template_name = 'projects/create_project.html'
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('project_list')


class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('project_list')


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')


class ProjectListView(ListView):
    model = Project
