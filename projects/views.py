from .models import Project

from django.views.generic.list import ListView


class ProjectListView(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        return context
