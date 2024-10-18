from flask import Flask, jsonify
import psycopg2
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def get_db_connection():
    try:
        app.logger.info("Attempting to connect to the database...")
        conn = psycopg2.connect(
            host="db",
            database="postgres_db",
            user="shreyak",
            password="shreyak"
        )
        app.logger.info("Database connection successful!")
        return conn
    except psycopg2.DatabaseError as e:
        app.logger.error(f"Database connection failed: {e}")
        return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    try:
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        conn.close()
        return jsonify(db_version=db_version[0])
    except Exception as e:
        app.logger.error(f"Error executing query: {e}")
        return jsonify({"error": "Failed to execute query"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
