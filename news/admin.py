from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'course', 'created_on')
    list_filter = ('created_on', 'course')
    date_hierarchy = 'created_on'
    prepopulated_fields = {'slug': ('title',)}
    
    def get_form(self, request, obj=None, **kwargs):
        """
        Override to limit the 'author' field dropdown to only the logged-in user.
        """
        form = super(NewsAdmin, self).get_form(request, obj, **kwargs)
        user = request.user

        if not user.is_superuser:
            form.base_fields['author'].queryset = form.base_fields['author'].queryset.filter(id=user.id)
        return form


