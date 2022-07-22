def network_alert_stub(celcius):
    print("testing-environment")
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius < 100:
        return 200
    return 500


class Alerter:

    def __init__(self):
        self.alert_failure_count = 0

    def alert_in_celcius(self, farenheit, environment):
        celcius = (farenheit - 32) * 5 / 9
        returnCode = network_alert_stub(celcius)
        if returnCode != 200:
            # non-ok response is not an error! Issues happen in life!
            # let us keep a count of failures to report
            # However, this code doesn't count failures!
            # Add a test below to catch this bug.Alter the stub above,if needed.
            self.alert_failure_count += 1
