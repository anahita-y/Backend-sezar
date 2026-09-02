from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['year' , 'title' , 'status' , 'status_badge']
    list_filter = ['status' , 'year']
    list_editable = ['status']
    search_fields  = ['title' , 'short_description']
    ordering = ['-year']

    def status_badge(self , obj):
        if obj.status == 'C':
            return 'تکمیل شد!'
        return 'درحال انجام!'
    status_badge.short_description = 'وضعیت نمایش'
    