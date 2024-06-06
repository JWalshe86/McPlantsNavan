from django.contrib import admin
from .models import Plant, Category, SeasonalEvent, PlantReview


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


class PlantReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "plant", "review", "rating")


admin.site.register(SeasonalEvent, SeasonalEventAdmin)
admin.site.register(PlantReview, PlantReviewAdmin)


admin.site.register(Plant, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
