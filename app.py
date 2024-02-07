from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'b1346c8d27a9b60d42f3abed77109a47'
BASE_URL = 'http://api.exchangerate.host/convert'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])

    api_url = BASE_URL.format(from_currency)
    response = requests.get(api_url, params={'access_key': API_KEY, 'from': from_currency, 'to': to_currency, 'amount': amount})
    data = response.json()

    if response.status_code == 200:
        converted_amount = data['result']

        return jsonify({'converted_amount': converted_amount})
    else:
        return jsonify({'error': 'Unable to fetch exchange rates'})

if __name__ == '__main__':
    app.run(debug=True)
