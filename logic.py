import requests

class CalculatorLogic:
    def __init__(self):
        self.expression = ""

    def clear(self):
        self.expression = ""

    def append(self, value):
        self.expression += str(value)

    def evaluate(self):
        try:
            return str(eval(self.expression))
        except Exception:
            return "Error"

    def convert_currency(self, amount, from_currency, to_currency):
        try:
            url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
            response = requests.get(url)
            data = response.json()
            return str(data.get("result", "Error"))
        except:
            return "Error"

    def get_crypto_price(self, symbol):
        try:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
            response = requests.get(url)
            data = response.json()
            return str(data[symbol]["usd"])
        except:
            return "Error"
