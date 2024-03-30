from django.test import TestCase
from django.core.mail import outbox
from django.core import mail
from django.urls import reverse


class WikipediaSummaryTestCase(TestCase):
    def test_summary_generation(self):
        response = self.client.get(reverse('get_wikipedia_summary'), {'title': 'Napoleon'})

        self.assertEqual(response.status_code, 200)

        self.assertIn('French emperor', response.content.decode())
        self.assertIn('military commander', response.content.decode())

    def test_alert_email(self):
        mail.outbox.clear()

        response = self.client.get(reverse('get_wikipedia_summary'), {'title': 'Napoleon'})

        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, 'Alert: Wikipedia Summary')
        self.assertIn('There are too many words of 5 letters and more', mail.outbox[0].body)

    def test_page_not_found(self):
        response = self.client.get(reverse('get_wikipedia_summary'), {'title': 'NonExistentPage'})

        self.assertEqual(response.status_code, 404)

