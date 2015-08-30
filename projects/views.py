from django.shortcuts import render
from .models import Project


def list_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/list_projects.html', {'projects': projects})
