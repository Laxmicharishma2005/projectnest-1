from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017')
db = client['Travelblog']

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        if 'name' not in data or 'rating' not in data or 'review' not in data:
            return jsonify({'message': 'Missing required fields'}), 400

        name = data['name']
        rating = data['rating']
        review = data['review']

        db.reviews.insert_one({
            'name': name,
            'rating': rating,
            'review': review,
        })

        return jsonify({'message': 'Data stored successfully'}), 200
    except Exception as e:
        print('Error:', e)
        return jsonify({'message': 'Data failed to store in the backend.'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')