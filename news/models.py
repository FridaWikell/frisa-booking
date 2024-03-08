from django.db import models
from django.contrib.auth.models import User
from booking.models import Course


class News(models.Model):
    """
    Django database model for news
    """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_update")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="news_course")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
