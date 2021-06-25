from django.contrib import admin
from shortener.models import SubmittedUrls


class SubmittedUrlsAdmin(admin.ModelAdmin):
    list_display = ['original_url', 'shorten_url', 'created_on', 'user']


admin.site.register(SubmittedUrls, SubmittedUrlsAdmin)
