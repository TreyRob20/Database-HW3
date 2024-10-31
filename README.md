Flask API for Fruit Basket Management
This API, built with Flask, interacts with PostgreSQL tables `basket_a` and `basket_b` to manage and query unique fruit entries in each basket. It provides endpoints for inserting new entries and retrieving unique fruits across both baskets.
Team Members
- Trey Roberts
- Nathaenal Prokop
  
Quick Start
1. **Database Setup**
Connect to PostgreSQL and create the required tables by executing the SQL commands below:

CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a) VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b) VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');
    
2. **Install Required Packages**
Ensure that the necessary Python packages are installed:
pip install flask psycopg2
3. **Run the Flask Application**
Start the API server by running:
python app.py
4. **Accessing the API**
With the server running, test the API endpoints using the examples below.
API Endpoints
1. **POST `/api/update_basket_a`**
Adds a new fruit to `basket_a`.
- **JSON Body Parameters:**
  - `fruit_a`: (string) The fruit’s name (default: 'Cherry').
  - `a`: (int) Unique integer ID for the fruit (default: 5).
- **Example Request:**
curl -X POST http://127.0.0.1:5000/api/update_basket_a -H "Content-Type: application/json" -d "{\"a\": 6, \"fruit_a\": \"Mango\"}"
- **Response:** Returns 'Success!' upon successful insertion or an error message if an issue occurs.
2. **GET `/api/unique`**
Retrieves distinct fruits from `basket_a` and `basket_b`.
- **Example Request:**
curl http://127.0.0.1:5000/api/unique
- **Response:** Renders an HTML page with lists of unique fruits from each basket.
Error Logging
Errors, such as database or request-handling issues, are recorded in `error.log`, allowing for easy troubleshooting.

