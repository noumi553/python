from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Load and prepare the data
df = pd.read_csv('home.csv')
df.columns = df.columns.str.strip()  # Clean column names

X = df['Size (sq.ft) (x)'].values.reshape(-1, 1)
y = df['Price ($) (y)'].values

# Train the model
model = LinearRegression()
model.fit(X, y)

# Home route
@app.route('/')
def home():
    return "🏠 House Price Predictor is Running!"

# Predict route (GET: /predict?size=3000)
@app.route('/predict', methods=['GET'])
def predict():
    try:
        size = float(request.args.get('size'))
        price = model.predict([[size]])[0]
        return jsonify({'Size (sq.ft)': size, 'Predicted Price ($)': round(price, 2)})
    except:
        return jsonify({'error': 'Invalid input. Please provide ?size=<number>'})

@app.route('/predict', methods=['POST'])
def predict_post():
    try:
        data = request.get_json()  # Get JSON data from POST body
        size = float(data['size'])  # Read 'size' value
        price = model.predict([[size]])[0]
        return jsonify({'Size (sq.ft)': size, 'Predicted Price ($)': round(price, 2)})
    except Exception as e:
        return jsonify({'error': 'Invalid input. Please send JSON like {"size": 3000}'}
if __name__ == "__main__":
                       app.run(debug=True)
