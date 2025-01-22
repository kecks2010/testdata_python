import sqlite3

connection = sqlite3.connect("testdata.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    birth_place TEXT,
    death_date DATE,
    death_place TEXT,
    phone_number TEXT,
    mobile_number TEXT,
    email_address TEXT UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    street TEXT,
    number TEXT,
    postal_code TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT,
    country TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_addresses (
    customer_id INTEGER NOT NULL,
    address_id INTEGER NOT NULL,
    address_type TEXT NOT NULL,
    PRIMARY KEY (customer_id, address_id),
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE,
    FOREIGN KEY (address_id) REFERENCES addresses(id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS login (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    two_factor_id TEXT,
    two_factor_type TEXT,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS payment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    account_owner TEXT NOT NULL,
    account_id TEXT NOT NULL,
    payment_provider TEXT NOT NULL,
    expiry_date TEXT,
    secure_code TEXT,
    payment_method TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
)
""")

connection.commit()
connection.close()

print("Datenbank und Tabellen wurden erfolgreich erstellt, falls sie noch nicht existieren.")
