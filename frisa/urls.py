"""
URL configuration for frisa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.template import loader


def homepage_view(request):
    """
    Render the index page
    """
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


urlpatterns = [
    path('about/', include('about.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls')),
    path('news/', include('news.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', homepage_view, name='home'),
]
