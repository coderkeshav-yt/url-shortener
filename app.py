import sqlite3
import string
import random
from flask import Flask, render_template, request, redirect

# --- Database Setup ---
def init_db():
    """Initializes the database and creates the 'urls' table if it doesn't exist."""
    conn = sqlite3.connect('/data/shortener.db') # Production path for Render's persistent disk
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT NOT NULL,
            short_code TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# --- Flask Application ---
app = Flask(__name__)

# --- Initialize Database on Startup ---
# This ensures the database and table exist before the first request.
init_db() # <-- THIS IS THE FIX

def get_db_connection():
    """Establishes a connection to the database."""
    conn = sqlite3.connect('/data/shortener.db') # Production path
    conn.row_factory = sqlite3.Row
    return conn

def generate_short_code(length=7):
    """Generates a unique random short code of a given length."""
    characters = string.ascii_letters + string.digits
    
    while True:
        short_code = ''.join(random.choices(characters, k=length))
        
        conn = get_db_connection()
        existing_code = conn.execute('SELECT short_code FROM urls WHERE short_code = ?', (short_code,)).fetchone()
        conn.close()
        
        if not existing_code:
            return short_code

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles the main page: form submission and displaying the result."""
    if request.method == 'POST':
        long_url = request.form['long_url']
        
        if not long_url:
            return render_template('index.html', error="URL cannot be empty.")

        conn = get_db_connection()
        
        existing_url = conn.execute('SELECT short_code FROM urls WHERE long_url = ?', (long_url,)).fetchone()
        
        if existing_url:
            short_code = existing_url['short_code']
        else:
            short_code = generate_short_code()
            conn.execute('INSERT INTO urls (long_url, short_code) VALUES (?, ?)', (long_url, short_code))
            conn.commit()
        
        conn.close()
        
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)
        
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Handles the redirection from the short URL to the original long URL."""
    conn = get_db_connection()
    url_data = conn.execute('SELECT long_url FROM urls WHERE short_code = ?', (short_code,)).fetchone()
    conn.close()

    if url_data:
        return redirect(url_data['long_url'])
    else:
        return "<h1>URL not found</h1>", 404