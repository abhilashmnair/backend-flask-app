# Backend Flask Application
This Flask application simulates a simplified data retrieval and processing system. It includes API endpoints to fetch data, process it, and retrieve the processed data.

## Features
- **/fetch-data**: Fetches mock data and processes it
- **/get-processed-data**: Retrieves the processed data stored in memory.

## Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment and activate the virtual environment
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the Flask application by running:

    ```bash
    python app.py
    ```

5. The application will run locally on `http://127.0.0.1:8080/`.

## API Endpoints

The mock data used is as follows:
    
```python
    {
        'cart' : [
            { 'id' : 101, 'name' : 'Apple iPhone 15 Pro', 'price' : 137600 },
            { 'id' : 102, 'name' : 'Apple Airpods Pro', 'price' : 24900 },
            { 'id' : 103, 'name' : 'Apple 20W USB-C Power Adapter', 'price' : 1900 },
            { 'id' : 104, 'name' : 'Apple iPhone 15 Pro Clear Case with MagSafe', 'price' : 4900 }
        ],
    }
```

### 1. Fetch and Process Data
- **Endpoint**: `/fetch-data`
- **Method**: `GET`
- **Description**: Simulates fetching data from an external service, processes the data and stores it in memory.
- **Response Example**:

    ```json
    {
        "message": "Fetched data is processed and stored"
    }
    ```

If an error occured while processing the data, the response will be:

```json
    {
        "message": "Error processing data"
    }
```

### 2. Retrieve Processed Data
- **Endpoint**: `/get-processed-data`
- **Method**: `GET`
- **Description**: Retrieves the processed data stored in memory.
- **Response Example**:

```json
    {
        "processed_data": {
            "cart": {
            "cart_total": 169300,
            "item_count": 4,
            "items": [
                {
                "id": 101,
                "name": "APPLE IPHONE 15 PRO",
                "price": 137600
                },
                {
                "id": 102,
                "name": "APPLE AIRPODS PRO",
                "price": 24900
                },
                {
                "id": 103,
                "name": "APPLE 20W USB-C POWER ADAPTER",
                "price": 1900
                },
                {
                "id": 104,
                "name": "APPLE IPHONE 15 PRO CLEAR CASE WITH MAGSAFE",
                "price": 4900
                }
            ]
            }
        }
    }
```

If no processed data is available, the response will be:

```json
    {
      "message": "No processed data available"
    }
```
