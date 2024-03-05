from django.shortcuts import render
from django.views import generic
from django.contrib.admin.views.decorators import staff_member_required
from .models import News

# Create your views here.
@staff_member_required
def news_list(request):
    news_items = News.objects.all()
    return render(request, 'news/news.html', {
        'news_items': news_items
    })
