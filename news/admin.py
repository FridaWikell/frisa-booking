from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'course', 'created_on')  # Fields to display in the list view
    list_filter = ('created_on', 'course')  # Fields to filter by in the list view
    date_hierarchy = 'created_on'
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
