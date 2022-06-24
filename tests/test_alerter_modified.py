from unittest import TestCase

from src.alerter_modified import Alerter


class TestAlerter(TestCase):

    def test_alerter(self):
        alert_obj = Alerter()
        alert_obj.alert_in_celcius(400.5, 'testing')
        alert_obj.alert_in_celcius(303.6, 'integration')
        print(f'{alert_obj.alert_failure_count} alerts failed.')
        self.assertEqual(Alerter().alert_failure_count, 6)
