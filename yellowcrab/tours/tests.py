from django.test import TestCase
from .models import ReportLine

# Create your tests here.


class ReportModelTests(TestCase):
    def test_shorten_description(self):
        line = ReportLine()

        line.description = None
        self.assertEqual(line.short_description(), None)

        line.description = ""
        self.assertEqual(line.short_description(), "")

        line.description = "012345"
        self.assertEqual(line.short_description(), "012345")

        line.description = "01234567"
        self.assertEqual(line.short_description(), "01234567")

        line.description = "012345678"
        self.assertEqual(line.short_description(), "012345678")

        line.description = "0123456789"
        self.assertEqual(line.short_description(), "0123456789")

        line.description = "01234567890"
        self.assertEqual(line.short_description(), "0123456...")
