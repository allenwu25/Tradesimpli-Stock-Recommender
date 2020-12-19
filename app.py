from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from recommender import get_similar

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    return 'Application running'



@app.route('/recommend', methods=['POST'])
@cross_origin()
def recommend():
    if request.method == 'POST':
        sym = request.get_json(force=True)['symbol']
        similar_stocks = get_similar(sym)
        return jsonify(similar_stocks)



if __name__ == "__main__":
    app.run()