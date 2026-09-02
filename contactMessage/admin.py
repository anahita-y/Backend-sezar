from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'topic' ,'status' , 'created_at']
    list_filter = ['status' , 'created_at']
    list_editable = ['status']
    readonly_fields = ['created_at']
    search_fields = ['name' , 'email' , 'topic' , 'messageText']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('اطلاعات فرستنده' , {'fields' : ('name' , 'email')}),
        ('محتوای پیام' , {'fields' : ('topic' , 'messageText')}),
        ('وضعیت' , {'fields' : ('status' , 'created_at'),
            'classes' : ('collapse',)}),
    )

#admin.site.register(ContactMessage)
