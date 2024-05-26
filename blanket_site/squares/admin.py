from django.contrib import admin
from squares.models import Square


class SquareAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "creator", "date_time_uploaded")


admin.site.register(Square, SquareAdmin)
