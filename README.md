Flask PostgreSQL Fruit Basket API
This project is a Flask API connected to a PostgreSQL database, enabling the addition of fruit data to a basket and retrieval of unique fruits in each basket. It includes error logging and a simple HTML template for displaying results.

Team Members

•	- Trey Roberts

•	- Nathaenal Prokop

Prerequisites
Python 3.6+
PostgreSQL with tables `basket_a` and `basket_b` in the `dvdrental` database.
Flask, Psycopg2, and Jinja2 libraries for Python.
Quick Start
1.	1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```
2.	2. Install Dependencies
```bash
pip install flask psycopg2
```
3.	3. Database Setup
Ensure PostgreSQL is running, and create tables if they don’t already exist:
```sql
CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR(100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR(100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a) VALUES
    (1, 'Apple'), (2, 'Orange'), (3, 'Banana'), (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b) VALUES
    (1, 'Orange'), (2, 'Apple'), (3, 'Watermelon'), (4, 'Pear');
```
4.	4. Run the Application
```bash
python app.py
```
5.	5. View the Application
- Open `http://127.0.0.1:5000/api/unique` in your browser to view unique fruits.
- To add a fruit to `basket_a`, send a POST request to `http://127.0.0.1:5000/api/update_basket_a` with a JSON payload.
Running the Application
6.	1. Start the Flask App
```bash
python app.py
```
7.	2. Access the Application
- **API endpoint to update `basket_a`**:
  - **URL**: `http://127.0.0.1:5000/api/update_basket_a`
  - **Method**: POST
  - **Payload (JSON)**:
    ```json
    {
      "fruit_a": "Grape",
      "a": 5
    }
    ```
  - **Response**: Returns `Success!` on successful insertion, otherwise an error message.

- **API endpoint to view unique fruits**:
  - **URL**: `http://127.0.0.1:5000/api/unique`
  - **Method**: GET
  - **Response**: HTML page displaying unique fruits in each basket.
File Structure
- `app.py` - Main Flask application
- `templates/unique.html` - HTML template for displaying unique fruits
- `error.log` - Log file for error tracking
Endpoints and Usage
1. **/api/update_basket_a** (POST)
   - Adds a fruit to `basket_a`.
   - Defaults:
     - `fruit_a`: "Cherry"
     - `a`: 5
2. **/api/unique** (GET)
   - Retrieves unique fruits from `basket_a` and `basket_b`.
   - Renders results on a simple HTML page.
Error Handling
All errors are logged to `error.log` in the format:
```
[Timestamp] - ERROR - <Error Message>
```
Example
To interact with the API, you can use tools like curl or Postman. Here are some example requests:
 Updating Basket A
   
    Use this endpoint to add a new fruit entry to basket_a. For example
    curl -X POST http://127.0.0.1:5000/api/update_basket_a -H "Content-Type: application/json" -d "{\"a\": 6, \"fruit_a\": \"Mango\"}"

This will insert a new row in basket_a with an ID of 6 and the fruit Mango. If successful, it will return "Success!" as a plain text response.
Retrieving Unique Fruits
Use the following endpoint to get a list of unique fruits from both basket_a and basket_b:

    curl http://127.0.0.1:5000/api/unique

This request will return an HTML page displaying distinct fruits in each basket.

