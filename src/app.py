from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'


def create_table():
    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create a 'users' table with 'id' and 'name' columns if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


@app.before_first_request
def initialize_database():
    # Call the create_table function before handling the first request
    create_table()


@app.route('/users', methods=['GET'])
def get_users():
    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Execute a SELECT query to fetch all users from the 'users' table
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    # Close the connection
    conn.close()

    # Return the users as JSON response
    return jsonify(users)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve the submitted name from the form
        name = request.form['name']

        # Connect to the SQLite database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert the submitted name into the 'users' table
        cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
        conn.commit()

        # Close the connection
        conn.close()

        # Redirect the user to the home page to prevent data resubmission
        return redirect(url_for('home'))

    # Fetch all users from the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Execute a SELECT query to fetch all names from the 'users' table
    cursor.execute('SELECT name FROM users')
    users = cursor.fetchall()
    users = [user[0] for user in users]

    # Close the connection
    conn.close()

    # Render the 'index.html' template with the list of users
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run()

