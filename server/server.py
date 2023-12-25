from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_locations', methods=['GET'])
def get_locations():
    response = jsonify({
        'locations': util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_price', methods = ['POST'])
def predict_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price':util.estimated_price(location,total_sqft,bhk,bath)
    })
    
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting Pyhton Flask Server For Home Price Prediction...")
    util.load_artifacts()
    app.run()



