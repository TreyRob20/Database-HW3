from flask import Flask, render_template, request, jsonify
import psycopg2
import psycopg2.extras
import logging

app = Flask(__name__)

# Set up logging for errors
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection
def get_db_connection():
    return psycopg2.connect(
        dbname="dvdrental",
        user="raywu1990",
        password="test",
        host="localhost"
    )

# Route to update basket_a with data from JSON payload
@app.route('/api/update_basket_a', methods=['POST'])
def update_basket_a():
    data = request.get_json()
    fruit_a = data.get('fruit_a', 'Cherry')  # Default to 'Cherry' if not provided
    a_value = data.get('a', 5)  # Default to 5 if not provided
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (%s, %s);", (a_value, fruit_a))
            conn.commit()
        return "Success!"  # Plain text response as required
    except Exception as e:
        logging.error("Error updating basket_a: %s", str(e))
        return str(e), 500  # Show PostgreSQL error message on the browser

# Route to show unique fruits in each basket
@app.route('/api/unique', methods=['GET'])
def unique_fruits():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT DISTINCT fruit_a FROM basket_a;")
                unique_a = [row[0] for row in cur.fetchall()]

                cur.execute("SELECT DISTINCT fruit_b FROM basket_b;")
                unique_b = [row[0] for row in cur.fetchall()]
        return render_template('unique.html', unique_a=unique_a, unique_b=unique_b)
    except Exception as e:
        logging.error("Error retrieving unique fruits: %s", str(e))
        return str(e), 500  # Show PostgreSQL error message on the browser

if __name__ == '__main__':
    app.run(debug=True)

