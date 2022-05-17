from django.contrib import admin
from .models import Biographies


@admin.register(Biographies)
class BiographiesAdmin(admin.ModelAdmin):
    pass
