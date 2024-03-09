from django.test import TestCase
from about.forms import ContactForm


class ContactFormTest(TestCase):
    def test_contact_form_valid_data(self):
        """
        Test the contact form with valid input data
        """
        form_data = {
            'first_name': 'Luke',
            'last_name': 'Skywalker',
            'email': 'luke@rebels.org',
            'content': 'I want to learn about the Force.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_data(self):
        """
        Test the contact form with invalid input data
        """
        form_data = {
            'first_name': '',
            'last_name': 'Skywalker',
            'email': 'not-an-email',
            'content': 'I want to learn about the Force.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['email'][0], 'Enter a valid email address.')

    def test_contact_form_email_field(self):
        """
        Test the contact form's email field
        with invalid and valid email addresses
        """
        form = ContactForm(data={'email': 'invalid-email'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        form = ContactForm(data={'email': 'luke@rebels.org'})
        form.data['first_name'] = 'Luke'
        form.data['last_name'] = 'Skywalker'
        form.data['content'] = 'Hello there!'
        self.assertTrue(form.is_valid())
        self.assertNotIn('email', form.errors)

    def test_contact_form_content_max_length(self):
        """
        Test the contact form's content field for max length constraint
        """
        content = 'a' * 10001
        form_data = {
            'first_name': 'Luke',
            'last_name': 'Skywalker',
            'email': 'luke@rebels.org',
            'content': content
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
        self.assertEqual(
            form.errors['content'][0],
            'Ensure this value has at most 10000 characters (it has 10001).')
