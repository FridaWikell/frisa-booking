from django.test import TestCase
from django.contrib.auth.models import User
from booking.models import Course
from .models import News
from django.utils import timezone


class NewsModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up data for the test
        """
        cls.user = User.objects.create_user(
            username='jedi_knight',
            email='jedi@example.com',
            password='theforce123')
        cls.course = Course.objects.create(
            name="Jedi Training",
            description="Learn the ways of the Force.")
        cls.news = News.objects.create(
            title="Galactic Republic Falls",
            slug="galactic-republic-falls",
            author=cls.user,
            course=cls.course,
            content=("This news item covers the fall of the Galactic Republic "
                     "and the rise of the Galactic Empire."),
            created_on=timezone.now()
        )

    def test_news_creation(self):
        """
        Test the creation of a news item and its fields
        """
        self.assertEqual(self.news.title, "Galactic Republic Falls")
        self.assertEqual(self.news.slug, "galactic-republic-falls")
        self.assertEqual(self.news.author, self.user)
        self.assertEqual(self.news.course, self.course)
        self.assertEqual(self.news.content,
                         ("This news item covers the fall of the Galactic "
                          "Republic and the rise of the Galactic Empire."))
        self.assertTrue(self.news.created_on)

    def test_news_string_representation(self):
        """
        Test the string representation of a news item
        """
        self.assertEqual(str(self.news), "Galactic Republic Falls")

    def test_news_ordering(self):
        """
        Test the default ordering of news items
        """
        second_news = News.objects.create(
            title="Rebellion Rises",
            slug="rebellion-rises",
            author=self.user,
            course=self.course,
            content=("This news item covers the rise of the Rebellion "
                     "against the Galactic Empire."),
            created_on=timezone.now() + timezone.timedelta(days=1)
        )
        latest_news = News.objects.first()
        self.assertEqual(latest_news, second_news,
                         ("News items are not ordered by "
                          "'created_on' descending."))
