from django.db import models
from datetime import datetime
import json

# Create your models here.

class ProjectManager(models.Manager):
    def createProjectFromJson(self, json_data):
        project = self.create(name = json_data['name'], client = json_data['client'],
                    operator = json_data['operator'],
                    address = json_data['address'],
                    start_time = datetime.strptime(json_data['start_time'], "%b %d, %Y %I:%M:%S %p"),
                    #end_time = json_data['end_time'],
                    status = json_data['status'],
                    datafolder = json_data['datafolder'])
        # TODO:
        # add end_time
        for observation in json_data['observations']:
            obs = Observation.objects.createObservationFromJson(project, observation)

        return project


class Project(models.Model):
    name = models.CharField(max_length = 200)
    client = models.CharField(max_length = 200)
    operator = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null = True)
    status = models.CharField(max_length = 200)
    datafolder = models.CharField(max_length = 200)
    objects = ProjectManager()

class LocationManager(models.Manager):
    def createLocationFromJson(self, json_data):
        location = self.create(address = json_data['address'])
        return location

class Location(models.Model):
    address = models.CharField(max_length = 200)
    objects = LocationManager()

class PipeManager(models.Manager):
    def createPipeFromJson(self, json_data):
        l = Location.objects.createLocationFromJson(json_data['location'])
        pipe = self.create(location = l,
                           pipe_dimension = json_data['pipe_dimension'],
                           spillwater = json_data['spillwater'],
                           daywater = json_data['daywater'],
                           upstream = json_data['upstream'],
                           cleansed_before = json_data['cleansed_before'],
                           previously_inspected = json_data['previously_inspected'])
        return pipe

class Pipe(models.Model):
    location = models.ForeignKey(Location)
    pipe_dimension = models.IntegerField()
    spillwater = models.BooleanField(default = False)
    daywater = models.BooleanField(default = False)
    upstream = models.BooleanField(default = False)
    cleansed_before = models.BooleanField(default = False)
    previously_inspected = models.BooleanField(default = False)

    objects = PipeManager()


class ObservationManager(models.Manager):
    def createObservationFromJson(self, project, json_data):
        pipe = Pipe.objects.createPipeFromJson(json_data['pipe'])
        observation = self.create(project=project, pipe=pipe,
                                  grade = json_data['grade'],
                                  distance = json_data['distance'],
                                  comment = json_data['comment'],
                                  picture = json_data['picture'])
        return observation

class Observation(models.Model):
    project = models.ForeignKey(Project)
    pipe = models.ForeignKey(Pipe)
    grade = models.CharField(max_length = 200)
    distance = models.IntegerField()
    comment = models.CharField(max_length = 200)
    picture = models.CharField(max_length = 200)

    objects = ObservationManager()
