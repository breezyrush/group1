from django.contrib import admin

# Register your models here.
class GenreAdmin(admin.AdminModel):
	pass
admin.site.register(Genre, GenreAdmin)