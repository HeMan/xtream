from django.shortcuts import render
from django.http import HttpResponse

from projects.models import Project

def index(request):
    project_list = Project.objects.all()
    print(project_list)
    output = ', '.join([p.name for p in project_list])

    return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the project index.")

def project(request, project_id):
    return HttpResponse("This is your report %s" % (project_id))
