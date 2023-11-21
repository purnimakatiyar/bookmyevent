import re
from dateutil import parser

def is_valid_username(username):
    return bool(re.match("^(?=.*[a-zA-Z0-9])(?!^\d+$)[a-zA-Z0-9]+$", username))

def check_valid_password(password):
    while True:
        if is_valid_password(password):
            return password
        else:
            print("Invalid password, please try again")
            
def is_valid_password(password):
    pattern = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[a-zA-Z\d!@#$%^&*(),.?":{}|<>]{8,}$'
    return bool(re.match(pattern, password))
    
    
def is_valid_name(name):
    return bool(re.match("^[a-zA-Z ]+$", name))

def is_valid_phone(phone):
    return bool(re.match("^[0-9]{10}$", phone))

def validate_event_name(event_name):
    return bool(event_name)

def validate_event_date(event_date):
    try:
        parser.parse(event_date)
        return True
    except ValueError:
        return False

def validate_event_rating(rating):
    return isinstance(rating, int) and 1 <= rating <= 10

def validate_event_price(price):
    return bool (re.match("^\d+$", price) and int(price) >= 0)

def validate_event_tickets(ticket_quantity):
    return (re.match("^\d+$", ticket_quantity) and int(ticket_quantity) > 0)