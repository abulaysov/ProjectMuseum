from django.contrib import admin
from .models import Authors, Pictures, Genre


class AuthorsAdmin(admin.ModelAdmin):
    pass


class PicturesAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Pictures, PicturesAdmin)
admin.site.register(Genre, GenreAdmin)