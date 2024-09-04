from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.get('/recipes')
def get_data():
    data = [
        {'Arecipe': 'Tzatziki', 'Ingredients': 'Greek Yogurt, Cucumber, Garlic, Lemon Juice, Olive Oil, Salt, Pepper', 'Instructions': 'Grate cucumber, mix with yogurt, garlic, lemon juice, olive oil, salt, and pepper. Serve chilled.'
        },
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)