import requests


class CurrencyConverter:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_rate(self, from_currency, to_currency):
        response = requests.get(f"{self.api_url}/{from_currency}")
        data = response.json()
        return data['rates'][to_currency]

    def convert(self, from_currency, to_currency, amount):
        rate = self.get_rate(from_currency, to_currency)
        return amount * rate

    def get_available_currencies(self):
        response = requests.get(f"{self.api_url}/USD")
        data = response.json()
        return list(data['rates'].keys())
