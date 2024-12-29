import random

def generate_random_number():
    try:
        # Dummy-Random-Number-Generator für Quanten
        random_number = random.randint(1, 1000)  # Zufallszahl zwischen 1 und 1000
        return {"random_number": random_number}, 200

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}, 500
