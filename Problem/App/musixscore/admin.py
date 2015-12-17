from django.contrib import admin

# Register your models here.
from .models import *


class CDAdmin(admin.ModelAdmin):
	pass		
admin.site.register(CD, CDAdmin)

class SongAdmin(admin.ModelAdmin):
	pass
admin.site.register(Song, SongAdmin)