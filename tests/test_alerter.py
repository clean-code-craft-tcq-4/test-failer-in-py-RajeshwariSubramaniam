from unittest import TestCase

from src.alerter import Alerter


class TestAlerter(TestCase):

    def test_alerter(self):
        a = Alerter()
        a.alert_in_celcius(400.5, 'production-environment')
        a.alert_in_celcius(303.6, 'integration-environment')
        print(f'{a.alert_failure_count} alerts failed.')
        self.assertEqual(a.alert_failure_count, 2)
