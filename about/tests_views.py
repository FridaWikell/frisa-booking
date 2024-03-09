from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail


class AboutViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('about')

    def test_about_view_get_request(self):
        """
        Test the about view responds to GET requests
        with the correct template and form
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
        self.assertIn('form', response.context)

    def test_about_view_post_request_valid_data(self):
        """
        Test the about view handles valid POST data correctly
        and sends an email
        """
        form_data = {
            'first_name': 'Luke',
            'last_name': 'Skywalker',
            'email': 'luke@rebels.org',
            'content': 'I am here to learn the ways of the Force.'
        }
        response = self.client.post(self.url, form_data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject, 'New message from contact form')

    def test_about_view_post_request_invalid_data(self):
        """
        Test the about view with invalid POST data
        """
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', 'first_name', 'This field is required.')
        self.assertFormError(
            response, 'form', 'last_name', 'This field is required.')
        self.assertFormError(
            response, 'form', 'email', 'This field is required.')
        self.assertFormError(
            response, 'form', 'content', 'This field is required.')

    def test_about_view_htmx_post_request(self):
        """
        Test the about view's response to a valid htmx POST request
        """
        form_data = {
            'first_name': 'Leia',
            'last_name': 'Organa',
            'email': 'leia@rebels.org',
            'content': 'May the Force be with you.'
        }
        response = self.client.post(
            self.url, form_data, HTTP_HX_REQUEST='true')
        self.assertIn('Whoa, that was fast!', response.content.decode())
