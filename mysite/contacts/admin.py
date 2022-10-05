from django.contrib import admin
from .models import Contacts, Category

# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'number', 'mail', 'category', 'created_at', 'is_published')
    list_display_links = ('name', 'job_title')
    search_fields = ('name', 'job_title')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Category, CategoryAdmin)