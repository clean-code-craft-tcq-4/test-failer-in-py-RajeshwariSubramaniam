def network_alert(celcius):
    """Uses real Network"""
    print(f"ALERT: Temperature is {celcius}°C in production")
    if celcius < 100:
        return 200
    return 500


def network_alert_stub(celcius):
    """Uses fake Network"""
    print(f"ALERT: Temperature is {celcius}°C in testing")
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius < 100:
        return 200
    return 500


class Alerter:
    def __init__(self):
        self.alert_failure_count = 0

    @staticmethod
    def temperature_in_celcius(farenheit):
        return (farenheit - 32) * 5 / 9

    def alert_counts(self, farenheit, environment):
        celcius = self.temperature_in_celcius(farenheit)
        if environment in ('production', 'production-environment', 'prod'):
            return_code = network_alert(celcius)
        else:
            return_code = network_alert_stub(celcius)
        if return_code != 200:
            # non-ok response is not an error! Issues happen in life!
            # let us keep a count of failures to report
            # However, this code doesn't count failures!
            # Add a test below to catch this bug.Alter the stub above,if needed.
            self.alert_failure_count += 1
        return self.alert_failure_count

    def print_alert_counts(self):
        print(f'{self.alert_failure_count} alerts failed.')
