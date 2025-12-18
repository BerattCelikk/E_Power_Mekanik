from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','date_sent')
    readonly_fields = ('name', 'email', 'message', 'date_sent')
    
admin.site.register(ContactMessage, ContactMessageAdmin)


    