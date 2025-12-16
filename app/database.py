import sqlite3
import os

# Get the database file path from the environment variable (injected by Secret)
DB_FILE = os.getenv("SQLITE_DATABASE_PATH")

def initialize_db():
    """Ensures the SQLite database file and a dummy table exist."""
    if not DB_FILE:
        print("CRITICAL: SQLITE_DATABASE_PATH environment variable is not set!")
        return False
        
    try:
        # Connect to the database file (creates it if it doesn't exist)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create a simple table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS status (
                id INTEGER PRIMARY KEY,
                message TEXT NOT NULL
            )
        ''')
        
        # Insert a dummy row if the table is empty
        cursor.execute("SELECT COUNT(*) FROM status")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO status (message) VALUES (?)", ("DB initialized successfully",))

        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"SQLite initialization failed: {e}")
        return False

def check_db_connection():
    """
    Checks if a connection can be established and a simple query runs.
    
    IMPORTANT: This function is now guaranteed to return a tuple (bool, str) 
    to prevent TypeError when the DB_FILE is missing during the Docker build test.
    """
    if not DB_FILE:
        # FIX: Return a 2-item tuple when the secret is missing (e.g., during 'RUN pytest' in Dockerfile)
        return False, "DB path missing (Secrets not available during build)"
        
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Attempt a simple read
        cursor.execute("SELECT message FROM status LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        return True, result[0] if result else "No data"
    except sqlite3.Error:
        return False, "Database connection failed"