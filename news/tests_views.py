from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import News, Course


class NewsListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up data for the entire test suite
        """
        cls.regular_user = User.objects.create_user(
            username='regular', password='password123')
        cls.staff_user = User.objects.create_user(
            username='staff', password='password123', is_staff=True)
        cls.super_user = User.objects.create_superuser(
            username='super', password='password123', is_superuser=True)
        cls.news_author = User.objects.create_user(
            username='news_author', password='password123', is_staff=True)
        cls.course = Course.objects.create(name="Interstellar Politics")

        News.objects.create(
            title="Public News",
            content="Public news content.",
            author=cls.news_author,
            course=cls.course
        )

        cls.url = reverse('news')

    def test_access_for_anonymous_user(self):
        """
        Ensure anonymous users cannot access the news list and are redirected
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_access_for_regular_user(self):
        """
        Ensure regular users cannot access the news list
        """
        self.client.login(username='regular', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_access_for_staff_user(self):
        """
        Ensure staff users can access the news list
        """
        self.client.login(username='staff', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news.html')

    def test_news_content_for_staff_user(self):
        """
        Ensure the correct news content is displayed to staff users
        """
        self.client.login(username='staff', password='password123')
        response = self.client.get(self.url)
        self.assertContains(response, "Public News")

    def test_access_for_superuser(self):
        """
        Ensure superusers can access the news list
        """
        self.client.login(username='super', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news.html')

    def test_news_content_for_superuser(self):
        """
        Ensure the correct news content is displayed to superusers
        """
        self.client.login(username='super', password='password123')
        response = self.client.get(self.url)
        self.assertContains(response, "Public News")
