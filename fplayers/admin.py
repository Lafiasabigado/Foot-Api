from django.contrib import admin

from fplayers.models import Player


# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname","date_of_birthday")

admin.site.register(Player,PlayerAdmin)