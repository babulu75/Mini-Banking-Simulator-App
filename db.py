# db.py
import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vinni@02#feb",
        database="bank"
    )
    cursor = conn.cursor()
    return conn, cursor
