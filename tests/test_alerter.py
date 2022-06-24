from unittest import TestCase

from src.alerter import Alerter


class TestAlerter(TestCase):

    def test_alerter(self):
        self.assertEqual(Alerter().alert_failure_count, 6)
