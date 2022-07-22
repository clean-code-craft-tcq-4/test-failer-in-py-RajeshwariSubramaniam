from unittest import TestCase

from src.alerter_modified import Alerter


class TestAlerter(TestCase):

    def test_alerter(self):
        alert_obj = Alerter()
        alert_obj.alert_counts(200, 'prod')
        alert_obj.alert_counts(400, 'test')
        alert_obj.alert_counts(500, 'stage')
        self.assertEqual(alert_obj.alert_failure_count, 2)
