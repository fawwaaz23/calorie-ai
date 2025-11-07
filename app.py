from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# simple AI calorie predictor (dummy for demo)
def estimate_calories(food_name):
    food_data = {
        "rice": 200, "chicken": 300, "apple": 95, "banana": 110,
        "idli": 70, "dosa": 160, "chapati": 100, "egg": 75
    }
    return food_data.get(food_name.lower(), random.randint(50, 400))

@app.route('/')
def home():
    return "🍎 Welcome to Calorie AI App!"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    food = data.get("food")
    calories = estimate_calories(food)
    return jsonify({"food": food, "estimated_calories": calories})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
