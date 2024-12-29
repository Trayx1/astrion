import hashlib

def generate_hash(text):
    if not text:
        return {"error": "Text is required"}, 400

    try:
        # SHA-256 Hash generieren
        sha256_hash = hashlib.sha256(text.encode()).hexdigest()
        return {"text": text, "hash": sha256_hash}, 200

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}, 500
