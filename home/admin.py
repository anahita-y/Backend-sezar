from django.contrib import admin
from .models import Profile, SiteDocument


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'role_title', 'is_available', 'availability_label']
    list_editable = ['is_available']
    search_fields = ['name', 'role_title', 'bio']
    list_filter = ['is_available']
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name', 'role_title', 'subtitle', 'bio')
        }),
        ('وضعیت دسترسی', {
            'fields': ('is_available', 'availability_label'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SiteDocument)
class SiteDocumentAdmin(admin.ModelAdmin):
    list_display = ['doc_type', 'title', 'file']
    list_editable = ['doc_type']
    list_display_links = ['title']
    list_filter = ['doc_type']
    search_fields = ['title']
    
    def doc_type_display(self, obj):
        icons = {
            'R': ' رزومه',
            'C': ' قرارداد',
            'T': ' تعرفه',
            'P': ' پکیج',
        }
        return icons.get(obj.doc_type, obj.doc_type)
    
    doc_type_display.short_description = 'نوع سند'