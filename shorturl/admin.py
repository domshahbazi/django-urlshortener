from django.contrib import admin
from shorturl.models import urlObj

# Register your models here.

class urlAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'date_created')
    search_fields = ['original_url']


admin.site.register(urlObj, urlAdmin)
