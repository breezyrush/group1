from django.contrib import admin
from .models import *

# Register your models here.
<<<<<<< HEAD
class PerformerAdmin(admin.ModelAdmin):
	pass
admin.site.register(Performer)
=======
from .models import *


class CDAdmin(admin.ModelAdmin):
	pass		
admin.site.register(CD, CDAdmin)

class SongAdmin(admin.ModelAdmin):
	pass
admin.site.register(Song, SongAdmin)
>>>>>>> 6f486dd87d00bfd6e886577d81488369f87cbb0c
