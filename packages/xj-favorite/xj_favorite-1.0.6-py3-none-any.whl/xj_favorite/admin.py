from django.contrib import admin
from .models import FavoriteSource, Favorite


class FavoriteSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    search_fields = ('id', 'value')
    fields = ('value',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'source_id', 'type', 'user_id')
    search_fields = ('id', 'source_id', 'type', 'user_id')
    fields = ('source_id', 'type', 'user_id')


# Register your models here.
admin.site.register(FavoriteSource, FavoriteSourceAdmin)
admin.site.register(Favorite, FavoriteAdmin)
