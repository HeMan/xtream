from django.db import models

# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length = 200)
	client = models.CharField(max_length = 200)
	operator = models.CharField(max_length = 200)
	address = models.CharField(max_length = 200)
	start_time = models.DateField()
	end_time = models.DateField()
	status = models.CharField(max_length = 200)
	datafolder = models.CharField(max_length = 200)

class Location(models.Model):
	address = models.CharField(max_length = 200)

class Pipe(models.Model):
	location = models.ForeignKey(Location)
	pipe_dimension = models.IntegerField()
	spillwater = models.BooleanField(default = False)
	daywater = models.BooleanField(default = False)
	upstream = models.BooleanField(default = False)
	cleansed_before = models.BooleanField(default = False)
	previously_inspected = models.BooleanField(default = False)

class Observation(models.Model):
	project = models.ForeignKey(Project)
	pipe = models.ForeignKey(Pipe)
	grade = models.CharField(max_length = 200)
	distance = models.IntegerField()
	comment = models.CharField(max_length = 200)
	picture = models.CharField(max_length = 200)
