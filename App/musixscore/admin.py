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

<<<<<<< HEAD

=======
class SongAdmin(admin.ModelAdmin):
	pass
admin.site.register(Song)
>>>>>>> 0ed92d4c94a19a5398b6027d820e2d17a3c980f4
