import sqlite3

databse = sqlite3.connect('foodbank.db')
cursor = databse.cursor()

def process_new_request(user_id, item_requested, quantity):
    try:
        cursor.execute(f'INSERT INTO requests ({user_id}, {item_requested}, {quantity})')
        return True
    except:
        return False

def get_all_requests():
    return cursor.execute('SELECT * FROM requests').fetchall()

def fufill_request(request_id, amount):
    c_amount = cursor.execute(f'SELECT amount FROM REQUESTS WHERE request_id = {request_id}').fetchall()
    if c_amount - amount <= 0:
        cursor.execute(f'UPDATE requests WHERE request_id = {request_id} status = "Fufilled"')
    else: 
        cursor.execute(f'UPDATE requests set amount = {c_amount - amount}')