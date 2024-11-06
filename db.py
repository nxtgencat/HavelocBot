import sqlite3

DATABASE = 'nxtgenspace.db'

def create_tables():
    """Create the users table if it doesn't already exist."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            chat_id INTEGER PRIMARY KEY,
            reg_number TEXT,
            shortlisted_companies TEXT
        )''')
        conn.commit()


def register_user(chat_id, reg_number):
    """Register or update the registration number for the given chat_id (only one reg_number per user)."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()

        # Check if the user already has a registration number
        c.execute('''SELECT reg_number FROM users WHERE chat_id = ?''', (chat_id,))
        result = c.fetchone()

        if result:
            # If the user already has a registration number, do not allow updating
            return False  # User already has a reg_number
        else:
            # If the user doesn't exist, create a new entry
            c.execute('''INSERT INTO users (chat_id, reg_number) VALUES (?, ?)''',
                      (chat_id, reg_number))
            conn.commit()
            return True  # New registration successful


def get_user_data(chat_id):
    """Retrieve user data based on chat_id."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT reg_number, shortlisted_companies FROM users WHERE chat_id = ?", (chat_id,))
        result = c.fetchone()
    return result


def delete_user_data(chat_id):
    """Delete user data from the database based on chat_id."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE chat_id = ?", (chat_id,))
        conn.commit()

        # Check if any rows were deleted
        if c.rowcount > 0:
            return True  # Data deleted
        else:
            return False  # No data found


def get_shortlisted_companies(chat_id, reg_number):
    """Retrieve shortlisted companies for a given reg_number."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT shortlisted_companies FROM users WHERE chat_id = ? AND reg_number = ?", (chat_id, reg_number))
        result = c.fetchone()
    return result


def get_all_registered_numbers():
    """Retrieve all registered numbers from the users table."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT reg_number FROM users")
        result = c.fetchall()
    return [reg[0] for reg in result]  # Return list of registration numbers
