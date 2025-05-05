import sqlite3

# Connect to the database (creates mikro.db if it doesn't exist)
conn = sqlite3.connect("mikro.db")
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone VARCHAR NOT NULL UNIQUE
    )
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
