from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Course, CourseSession, Booking
from datetime import timedelta


class BookingViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up data for the entire Test Case
        """
        cls.user = User.objects.create_user(
            username='testuser', password='12345')
        cls.course = Course.objects.create(
            name="Test Course", description="Test Course Description")
        cls.course_session = CourseSession.objects.create(
            course=cls.course,
            start_time=timezone.now() + timedelta(days=1),
            end_time=timezone.now() + timedelta(days=1, hours=3),
            spots_available=5
        )

        """
        Define another session that can be used to change the booking to
        """
        cls.another_session = CourseSession.objects.create(
            course=cls.course,
            start_time=timezone.now() + timedelta(days=3),
            end_time=timezone.now() + timedelta(days=3, hours=3),
            spots_available=5
        )
        cls.booking = Booking.objects.create(
            user=cls.user, course_session=cls.course_session)

    def test_list_courses_view(self):
        """
        Testing access to the list_courses view
        """
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.name)

    def test_book_session_view_redirects_for_anonymous_user(self):
        """
        Testing that anonymous users are redirected
        """
        response = self.client.get(reverse(
            'book_session', args=[self.course_session.id]))
        self.assertEqual(response.status_code, 302)

    def test_my_bookings_view(self):
        """
        Testing that the logged in user can access my_bookings
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.name)

    def test_book_session_creates_booking(self):
        """
        Testing that a booking is created upon a valid post request
        """
        self.client.login(username='testuser', password='12345')
        session_to_book = CourseSession.objects.create(
            course=self.course,
            start_time=timezone.now() + timedelta(days=10),
            end_time=timezone.now() + timedelta(days=10, hours=3),
            spots_available=5
        )
        response = self.client.post(reverse('book_session',
                                    args=[session_to_book.id]), follow=True)
        self.assertTrue(Booking.objects.filter(user=self.user,
                        course_session=session_to_book).exists())
        self.assertRedirects(response, reverse('success_page'))

    def test_edit_booking_view_redirects_for_anonymous_user(self):
        """
        Test to ensure that an anonymous user (not logged in) attempting
        to access the edit booking view is redirected
        """
        response = self.client.get(reverse(
            'edit_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 302)

    def test_edit_booking_view_for_valid_user(self):
        """
        Test to ensure that a logged-in user can access the edit booking view
        and the correct template is used to render the page
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse(
            'edit_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit_booking.html')

    def test_edit_booking_post_changes_booking(self):
        """
        Test to ensure that submitting the form on the edit booking view
        with a POST request correctly changes the booked session for the user
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse(
            'edit_booking', args=[self.booking.id]),
            {'session_id': self.another_session.id}, follow=True)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.course_session, self.another_session)
        self.assertRedirects(response, reverse('my_bookings'))

    def test_delete_booking_view_redirects_for_anonymous_user(self):
        """
        Test to verify that an anonymous user attempting to access
        the delete booking view is redirected
        """
        response = self.client.get(reverse(
            'delete_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_booking_view_for_valid_user(self):
        """
        Test to ensure that a logged-in user can delete a booking
        through a POST request to the delete booking view
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse(
            'delete_booking', args=[self.booking.id]), follow=True)
        self.assertFalse(Booking.objects.filter(id=self.booking.id).exists())
        self.assertEqual(CourseSession.objects.get(
            id=self.course_session.id).spots_available, 6)
        self.assertRedirects(response, reverse('my_bookings'))
