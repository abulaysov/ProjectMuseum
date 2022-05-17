from django.contrib import admin

from .models import Quotes


class QuotesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quotes, QuotesAdmin)