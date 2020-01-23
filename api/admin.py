from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Trash)
admin.site.register(TrashState)
admin.site.register(Schedule)
admin.site.register(Sector)
admin.site.register(Feedback)


