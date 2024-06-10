from django.contrib import admin


from .models import NewsletterUsers

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

admin.site.register(NewsletterUsers, NewsletterAdmin)

