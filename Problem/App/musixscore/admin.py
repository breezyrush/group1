from django.contrib import admin

# Register your models here.
from .models import CD


class CDAdmin(admin.ModelAdmin):
	pass		
admin.site.register(CD, CDAdmin)