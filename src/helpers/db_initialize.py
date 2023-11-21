from models.database import DBConnection
db = DBConnection
def create_auth_table():
    with db as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS Authenticate(user_id TEXT PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL, role TEXT NOT NULL)')
            
def create_user_details_table():
    with db as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS UserDetails(user_id TEXT PRIMARY KEY, username TEXT, name TEXT, phone INTEGER, FOREIGN KEY (user_id) REFERENCES Authentication(user_id))')
            
def create_event_table():
    with db as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS Events(event_id TEXT PRIMARY KEY, user_id TEXT, event_name TEXT, event_date TEXT, location TEXT, rating FLOAT, price FLOAT, category TEXT, ticket_qty INTEGER, FOREIGN KEY (user_id) REFERENCES Authentication(user_id))')
            
def create_booked_event_table():
    with db as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS BookedEvents(booking_id TEXT PRIMARY KEY, user_id TEXT, event_id TEXT, event_name TEXT, event_date TEXT, ticket_qty INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES Authentication(user_id), FOREIGN KEY (event_id) REFERENCES Events(event_id))')
      
create_auth_table()
create_event_table()
create_user_details_table()
create_booked_event_table()     