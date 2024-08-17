# -------------------------------------------------------------------------------------
# © 2024 Abhilash Nair. All rights reserved.
# 
# Licensed under the MIT License. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at:
# 
# http://opensource.org/licenses/MIT
# 
# This software is provided "AS IS," without any warranties or conditions of any kind.
# -------------------------------------------------------------------------------------

# Import all necessary libraries for the app
# For flask applications we import Flask, jsonify to return JSON data as response
# and request for processing the imcoming requests  
from flask import Flask, jsonify, request
import os

# Create a Flask application instance
app = Flask(__name__)

# Mock data to simulate data fetched from an external service, For demo purpose, we have simulated a 
# checkout cart of a user. The data includes:
#   - ID    : A unique id for each item
#   - Name  : The name of the item in the cart
#   - Price : The price of the item
mock_data = {
    'cart' : [
        { 'id' : 101, 'name' : 'Apple iPhone 15 Pro', 'price' : 137600 },
        { 'id' : 102, 'name' : 'Apple Airpods Pro', 'price' : 24900 },
        { 'id' : 103, 'name' : 'Apple 20W USB-C Power Adapter', 'price' : 1900 },
        { 'id' : 104, 'name' : 'Apple iPhone 15 Pro Clear Case with MagSafe', 'price' : 4900 }
    ],
}

# Mock memory storage to store the processed data
mock_memory_storage = {}

def processData(data):
    """
    This function takes the fetched data and applies transformation on it.
    The processing involves converting the item names to uppercase and summing the prices along with total count
        The processed data is then stored in memory.
    """

    # Variable to store the total cart value
    totalPrice = 0

    # Loop through each item in the cart, converting the item names to uppercase
    # and add the price of item to the total cart value
    for item in data['cart']:
        totalPrice += item['price']
        item['name'] = item['name'].upper()
    
    mock_memory_storage['cart'] = {
        'cart_total' : totalPrice,
        'item_count' : len(data['cart']),
        'items' : data['cart']
    }

@app.route('/', methods = ['GET'])
def home():
    """
    API Endpoint : /
    Methods      : GET
    Description  : Mostly used as a homepage or landing page endpoint
    """
    return('Home Page')

@app.route('/fetch-data', methods = ['GET'])
def fetchData():
    """    
    API Endpoint : /fetch-data
    Method       : GET
    Description  : Simulates fetching data from an external service and processing it.
    Returns      : JSON response with a success message and the processed data.
    """

    # This should be replaced by a function or API call to the external service for fetching the data
    fetchedData = mock_data

    if(fetchedData):
        try:
            # Call the function to process the data
            processData(fetchedData)
            return jsonify({"message": "Fetched data is processed and stored"}), 200
        except Exception as e:
            # Set status code as 500 since its an internal error with the server with data processing
            return jsonify({"message": "Error processing data", "error": str(e)}), 500
    else:
        # If no data is fetched, return a 500 error
        return jsonify({"message": "No data received from service"}), 500

@app.route('/get-processed-data', methods = ['GET'])
def getProcessedData():
    """
    API Endpoint : /get-processed-data
    Method       : GET
    Description  : Retrieves the processed data from in-memory storage. Returns error, if data is available
    Returns      : JSON response with the processed data or an error message.
    """

    if mock_memory_storage:
        # Return the processed data if available
        return jsonify({"processed_data": mock_memory_storage}), 200
    else:
        # Return an error message if no data is available
        return jsonify({"message": "No processed data available"}), 404

if __name__ == "__main__":
    """
    Entry point of the Flask application.
    The application will run on the host and port specified by environment variables,
    or default to '0.0.0.0' and port 8080 if not specified.
    """
    # Retrieve host and port from environment variables, with defaults
    host = os.getenv('FLASK_HOST', '0.0.0.0')  # Defaults to '0.0.0.0'
    port = int(os.getenv('FLASK_PORT', 8080))  # Defaults to 8080

    # Run the Flask application with specified host and port
    app.run(host = host, port = port, debug = True)