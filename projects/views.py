from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Project


class ProjectCreate(CreateView):
    template_name = 'projects/create_project.html'
    model = Project
    fields = ['title', 'description', 'max_members', 'difficulty',
              'image', 'participants', 'coach']
    success_url = reverse_lazy('project_list')


class ProjectUpdate(UpdateView):
    template_name = 'projects/update_project.html'
    model = Project
    fields = ['title', 'description', 'max_members', 'difficulty',
              'image', 'participants', 'coach']
    success_url = reverse_lazy('project_details')


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project
