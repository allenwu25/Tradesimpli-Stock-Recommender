from flask import Flask, request, jsonify
app = Flask(__name__)
from recommender import get_similar

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        sym = request.get_json(force=True)['symbol']
        similar_stocks = get_similar(sym)
        return jsonify(similar_stocks)



if __name__ == "__main__":
    app.run()