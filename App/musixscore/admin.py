from django.contrib import admin
from .models import *

# Register your models here.
class PerformerAdmin(admin.ModelAdmin):
	pass
admin.site.register(Performer)

class GenreAdmin(admin.ModelAdmin):
	pass
admin.site.register(Genre)

class CDAdmin(admin.ModelAdmin):
	pass
admin.site.register(CD)

class SongAdmin(admin.ModelAdmin):
	pass
admin.site.register(Song)
