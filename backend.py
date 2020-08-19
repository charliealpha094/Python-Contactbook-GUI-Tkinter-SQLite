# Done by Carlos Amaral (18/08/2020)
import sqlite3


# Create a database and it's connection and also a cursor
def connection():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, phone INTEGER, email TEXT)")
    conn.commit()
    conn.close()


# Function to add a contact to our contacts database
def submit(name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts VALUES(NULL,?,?,?)", (name, phone, email))
    conn.commit()
    conn.close()


# Function to let the user visualize all the contacts inside the database
def view():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    records = cursor.fetchall()
    conn.commit()
    conn.close()
    return records


# Function to update a Contact
def update(id, name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, id))
    conn.commit()
    conn.close()


# Function to delete a Contact
def delete(id):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (id,))
    conn.commit()
    conn.close()


# Function to Search for a Contact inside the Database
def search(name=""):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%'+name+'%',))
    records = cursor.fetchall()
    conn.close()
    return records


connection()
