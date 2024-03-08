from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import News


@staff_member_required
def news_list(request):
    """
    Render all news if the logged in user is and is a staff member or superuser.
    """
    news_items = News.objects.all()
    return render(request, 'news/news.html', {
        'news_items': news_items
    })
