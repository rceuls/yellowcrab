from django.test import TestCase

# Create your tests here.


class ReportModelTests(TestCase):
    def test_base_calculation(self):
        self.assertIs(1 + 1, 2)
