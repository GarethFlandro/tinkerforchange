import sqlite3

database = sqlite3.connect('foodbank.db')
cursor = database.cursor()

def process_new_request(user_id, item_requested, quantity):
    try:
        cursor.execute('INSERT INTO requests (user_id, item_requested, quantity) VALUES (?, ?, ?)', (user_id, item_requested, quantity))
        database.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def get_all_requests():
    try:
        return cursor.execute("SELECT * FROM requests WHERE status != 'Fulfilled'").fetchall()
    except Exception as e:
        print(f"Error: {e}")
        return []
    
def fulfill_request(request_id, amount):
    try:
        c_amount_result = cursor.execute('SELECT quantity FROM requests WHERE request_id = ?', (request_id,)).fetchone()
        if c_amount_result is not None:
            c_amount = c_amount_result[0]
            if c_amount - amount <= 0:
                cursor.execute('UPDATE requests SET status = "Fulfilled" WHERE request_id = ?', (request_id,))
                user_id_result = cursor.execute('SELECT user_id FROM requests WHERE request_id = ?', (request_id,)).fetchone()
                if user_id_result is not None:
                    user_id = user_id_result[0]
                    email_result = cursor.execute('SELECT email FROM users WHERE user_id = ?', (user_id,)).fetchone()
                    if email_result is not None:
                        email = email_result[0]
                        send_email(email, 'Your request has been fulfilled')
            else:
                cursor.execute('UPDATE requests SET quantity = quantity - ? WHERE request_id = ?', (amount, request_id))
            database.commit()
    except Exception as e:
        print(f"Error: {e}")

def send_email(email, message):
    pass

# CREATE TABLE requests (
#     request_id INT AUTO_INCREMENT PRIMARY KEY,
#     user_id INT,
#     request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     item_requested VARCHAR(255) NOT NULL,
#     quantity INT NOT NULL,
#     status VARCHAR(50) DEFAULT 'pending', -- e.g., 'pending', 'approved', 'denied', 'fulfilled'
#     FOREIGN KEY (user_id) REFERENCES users(user_id)
# );
# CREATE TABLE users (
#     user_id INT AUTO_INCREMENT PRIMARY KEY,
#     full_name VARCHAR(255) NOT NULL,
#     email VARCHAR(255),
#     phone VARCHAR(20),
#     address TEXT,
#     registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
