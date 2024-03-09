from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from booking.models import Course
from .models import News
from .admin import NewsAdmin


class MockRequest:
    def __init__(self, user=None):
        self.user = user


class NewsAdminTests(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.user = User.objects.create_user(
            username='user',
            password='password',
            is_staff=True)
        self.superuser = User.objects.create_superuser(
            username='superuser',
            password='password')

        self.course = Course.objects.create(name="Galactic History")

        self.news_item = News.objects.create(
            title="The Galactic Empire Rises",
            slug="the-galactic-empire-rises",
            author=self.user,
            course=self.course,
            content=("A long time ago in a galaxy far, far away... "
                     "The Republic has fallen, and in its place, the Galactic "
                     "Empire has risen, promising order and security.")
        )

    def test_get_form_limited_to_logged_in_user(self):
        """
        Test that the author field is limited
        to the logged-in user for non-superusers
        """
        ma = NewsAdmin(News, self.site)
        request = MockRequest(user=self.user)
        form = ma.get_form(request)
        self.assertEqual(
            form.base_fields['author'].queryset.count(), 1)
        self.assertEqual(
            form.base_fields['author'].queryset.first(), self.user)

    def test_get_form_all_users_for_superuser(self):
        """
        Test that the author field includes all users for superusers
        """
        ma = NewsAdmin(News, self.site)
        request = MockRequest(user=self.superuser)
        form = ma.get_form(request)
        self.assertTrue(form.base_fields['author'].queryset.count() > 1)

    def test_get_queryset_for_superuser(self):
        """
        Test that superusers can see all news items
        """
        ma = NewsAdmin(News, self.site)
        request = MockRequest(user=self.superuser)
        qs = ma.get_queryset(request)
        self.assertEqual(qs.count(), News.objects.count())

    def test_get_queryset_limited_for_regular_user(self):
        """
        Test that regular users can only see their own news items
        """
        another_user = User.objects.create_user(
            username='another_user',
            password='password',
            is_staff=True)
        News.objects.create(
            title="Rebellion's Victory at Endor",
            slug="rebellions-victory-at-endor",
            author=another_user,
            course=self.course,
            content="The Rebel Alliance has scored a crucial victory "
                    "by destroying the second Death Star near Endor."
        )

        ma = NewsAdmin(News, self.site)
        request = MockRequest(user=self.user)
        qs = ma.get_queryset(request)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.news_item)
