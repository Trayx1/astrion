# backend/tools/blockchain.py
import random

def check_wallet_balance(wallet_address):
    if not wallet_address:
        return {"error": "Wallet address is required"}, 400
    # Dummy logic for balance (simulating an API call)
    balance = f"{random.uniform(0.01, 10):.3f} ETH"
    return {"wallet_address": wallet_address, "balance": balance}, 200

def get_token_price(token_symbol):
    if not token_symbol:
        return {"error": "Token symbol is required"}, 400

    # Dummy token prices (in USD)
    token_prices = {
        "ETH": 1234.56,
        "BTC": 28901.23,
        "USDT": 1.00,
        "BNB": 238.12
    }

    price = token_prices.get(token_symbol.upper())
    if price:
        return {"token": token_symbol.upper(), "price": f"${price:.2f}"}, 200
    else:
        return {"error": f"Price for {token_symbol.upper()} not found"}, 404
