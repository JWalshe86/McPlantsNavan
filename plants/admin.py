from django.contrib import admin
from .models import Plant, Category, SeasonalEvent


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class SeasonalEventAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date")


admin.site.register(SeasonalEvent, SeasonalEventAdmin)


admin.site.register(Plant, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
