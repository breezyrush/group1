from django.contrib import admin
from .models import *

# Register your models here.
class PerformerAdmin(admin.ModelAdmin):
	pass
admin.site.register(Performer)

class GenreAdmin(admin.ModelAdmin):
	pass
admin.site.register(Genre)