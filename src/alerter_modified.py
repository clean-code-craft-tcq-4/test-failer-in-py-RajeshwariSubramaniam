
class Network:
    def __init__(self, temperature):
        self.celcius = temperature

    def network_alert(self):
        """Uses real Network"""
        print(f"ALERT: Temperature is {self.celcius}°C")
        if self.celcius < 100:
            return 200
        return 500

    def network_alert_stub(self):
        """Uses fake Network"""
        print(f"ALERT: Temperature is {self.celcius}°C")
        # Return 200 for ok
        # Return 500 for not-ok
        # stub always succeeds and returns 200
        if self.celcius < 100:
            return 200
        return 500


class Alerter:

    def __init__(self):
        self.alert_failure_count = 0

    def alert_in_celcius(self, farenheit, environment):
        celcius = (farenheit - 32) * 5 / 9
        network_obj = Network(temperature=celcius)
        print(f"Current environment is set to {environment}")
        if environment == 'integration':
            returnCode = network_obj.network_alert()
        else:
            returnCode = network_obj.network_alert_stub()
        if returnCode != 200:
            # non-ok response is not an error! Issues happen in life!
            # let us keep a count of failures to report
            # However, this code doesn't count failures!
            # Add a test below to catch this bug.Alter the stub above,if needed.
            self.alert_failure_count += 0



