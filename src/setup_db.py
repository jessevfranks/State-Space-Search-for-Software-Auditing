import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create user table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
)
''')

# Insert the "admin" user
cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ('admin', 'very_coMplEX_passWoRd_123')
)

conn.commit()
conn.close()

print("users.db created successfully with admin user")



