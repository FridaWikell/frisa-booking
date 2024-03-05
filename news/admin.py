from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
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

    def get_queryset(self, request):
        """
        Override to limit the queryset to only show items authored by the logged-in user.
        """
        qs = super(NewsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers see all items.
        return qs.filter(author=request.user)  # Other users see only their items.


