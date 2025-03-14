from django.shortcuts import render

# Create your views here.

from .models import Bug, Project
from django.http import HttpResponse


def bug_list(request):
    bugs = Bug.objects.all()
    output = ', '.join([bug.title for bug in bugs])
    return HttpResponse(output)


def project_list(request):
    projects = Project.objects.all()
    output = ', '.join([project.name for project in projects])
    return HttpResponse(output)
