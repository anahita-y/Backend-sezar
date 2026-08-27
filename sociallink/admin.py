from django.contrib import admin
from .models import SocialLink

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform' , 'url_or_value' , 'label' , 'has_map']
    list_editable = ['label']
    search_fields = ['platform' , 'label' , 'url_or_value']

    def has_map(self , obj):
        return bool(obj.map_link)
    has_map.boolean = True
    has_map.short_description = 'نقشه دارد؟'
#admin.site.register(SocialLink)
