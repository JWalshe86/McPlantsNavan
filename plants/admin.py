from django.contrib import admin
from django.contrib.auth.models import User
from .models import Plant, Category, SeasonalEvent, PlantReview, Stock


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

    # only user can see name in dropdown - credit Born TO Code
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class StockAdmin(admin.ModelAdmin):
    list_display = ("plant", "units")


admin.site.register(SeasonalEvent, SeasonalEventAdmin)
admin.site.register(PlantReview, PlantReviewAdmin)


admin.site.register(Plant, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Stock, StockAdmin)
