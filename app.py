from flask import Flask, request, jsonify
from converter import CurrencyConverter


app = Flask(__name__)

converter = CurrencyConverter(api_url="https://api.exchangerate-api.com/v4/latest")


@app.route('/api/rates', methods=['GET'])
def get_rate():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('value'))

    if not from_currency or not to_currency or not amount:
        return jsonify({"error": "Missing required parameters"}), 400

    result = converter.convert(from_currency, to_currency, amount)
    return jsonify({"result": result})


@app.route('/api/currencies', methods=['GET'])
def get_currencies():
    currencies = converter.get_available_currencies()
    return jsonify({"currencies": currencies})


if __name__ == '__main__':
    app.run(debug=True)
