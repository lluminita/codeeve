from .models import Project

from django.views.generic.list import ListView


class ProjectListView(ListView):
    model = Project
