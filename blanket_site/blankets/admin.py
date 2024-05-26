from django.contrib import admin
from blankets.models import Blanket, BlanketItem


class BlanketAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "num_cols", "num_rows")


class BlanketItemAdmin(admin.ModelAdmin):
    list_display = ("id", "square", "blanket", "column", "row")


admin.site.register(Blanket, BlanketAdmin)
admin.site.register(BlanketItem, BlanketItemAdmin)
