from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, CourseSession, Booking
from django.utils import timezone
from datetime import timedelta


class CourseModelTest(TestCase):
    def test_string_representation(self):
        """
        Tests that the string representation of a Course object
        matches its name
        """
        course = Course.objects.create(
            name="Star Wars for Beginners",
            description="Learn the basics of the Star Wars universe.")
        self.assertEqual(str(course), "Star Wars for Beginners")


class CourseSessionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up a Course object for use in test methods
        """
        cls.course = Course.objects.create(
            name="Yoda's Force Class",
            description="Master the Force with guidance from Yoda.")
        cls.session_start = timezone.now() + timedelta(days=1)
        cls.session_end = cls.session_start + timedelta(hours=4)

    def test_string_representation(self):
        """
        Tests that the string representation of a CourseSession
        includes the course name and start time
        """
        session = CourseSession.objects.create(
            course=self.course,
            start_time=self.session_start,
            end_time=self.session_end,
            spots_available=10
        )
        expected_string = (
            f"Yoda's Force Class - "
            f"{self.session_start.strftime('%Y-%m-%d %H:%M')}"
        )
        self.assertEqual(str(session), expected_string)


class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up User, Course, and CourseSession objects for use in test methods
        """
        cls.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='secret')
        cls.course = Course.objects.create(
            name="The Droids You're Looking For: Robotics in Star Wars",
            description="Explore robotics through the droids of Star Wars.")
        cls.session = CourseSession.objects.create(
            course=cls.course,
            start_time=timezone.now() + timedelta(days=5),
            end_time=timezone.now() + timedelta(days=5, hours=3),
            spots_available=15
        )

    def test_booking_creation(self):
        """
        Tests that a Booking object is correctly created with a user,
        course session, and automatic booking date
        """
        booking = Booking.objects.create(
            user=self.user,
            course_session=self.session
        )
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.course_session, self.session)
        self.assertTrue(booking.booking_date)
