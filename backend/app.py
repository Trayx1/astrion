from flask import Flask, jsonify, request
from flask_cors import CORS
from tools import blockchain, network, cryptography, ai, quantum, utilities

app = Flask(__name__)
CORS(app)

# Root Endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Astrion API"}), 200

# Blockchain Routes
@app.route('/api/blockchain/wallet_balance', methods=['POST'])
def wallet_balance():
    data = request.json
    wallet_address = data.get("wallet_address")
    return blockchain.check_wallet_balance(wallet_address)

# Token Price Checker Route
@app.route('/api/blockchain/token_price', methods=['POST'])
def token_price():
    data = request.json
    token_symbol = data.get("token_symbol")
    return blockchain.get_token_price(token_symbol)

# Network Routes
@app.route('/api/network/url_to_ip', methods=['POST'])
def url_to_ip():
    data = request.json
    url = data.get("url")
    return network.url_to_ip(url)

@app.route('/api/network/ip_to_location', methods=['POST'])
def ip_to_location():
    data = request.json
    ip = data.get("ip")
    return network.ip_to_location(ip)


# Hash Generator Route
@app.route('/api/cryptography/hash', methods=['POST'])
def generate_hash():
    data = request.json
    text = data.get("text")
    return cryptography.generate_hash(text)


# Text Summarizer Route
@app.route('/api/ai/summarize', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get("text")
    return ai.summarize_text(text)

# Sentiment Analyzer Route
@app.route('/api/ai/sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get("text")
    return ai.analyze_sentiment(text)

# Quantum Random Number Generator Route
@app.route('/api/quantum/random_number', methods=['GET'])
def quantum_random_number():
    return quantum.generate_random_number()


# Utilities Routes
@app.route('/api/utilities/convert_timezone', methods=['POST'])
def convert_timezone():
    data = request.json
    time = data.get("time")
    timezone = data.get("timezone")
    return utilities.convert_timezone(time, timezone)

if __name__ == '__main__':
    app.run(debug=True)
