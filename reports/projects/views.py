from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.template import add_to_builtins

add_to_builtins('ember.templatetags.ember')

from projects.models import *

def index(request):
    project_list = Project.objects.all()

    template = loader.get_template('projects/index.html')
    context = RequestContext(request, {
                'project_list': project_list,
            })
    return HttpResponse(template.render(context))

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    observations = project.observation_set.all()
    print(project.name)
    template = loader.get_template('projects/project.html')
    context = RequestContext(request, {
                'project': project,
                'observations': observations,
            })
    return HttpResponse(template.render(context))
