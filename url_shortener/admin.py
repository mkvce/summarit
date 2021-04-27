from django.contrib import admin
from url_shortener.models import URL, UserProfile, Code

# Register your models here.


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('label', 'user', 'jcreated', 'short')
    search_fields = ('label',)
    ordering = ('-created',)


admin.site.register(UserProfile)
