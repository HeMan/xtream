from django.contrib import admin

# Register your models here.
from projects.models import *

admin.site.register(Project)
admin.site.register(Observation)
admin.site.register(Pipe)
admin.site.register(Location)

