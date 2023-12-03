from settings.config import queries
from models.database import DBConnection
from utils.uuid_generator import generate_uuid


class BookedEvents:
    
    
    def __init__(self, **kwargs: dict) -> None: 
        self.booking_id = generate_uuid()
        self.user_id = kwargs.get('user_id')
        self.event_id = kwargs.get('event_id')
        self.ticket_quantity = kwargs.get('ticket_quantity')
        self.db = DBConnection()
        
    
    def view_booked_events(self, user_id: str) -> tuple:
        '''This method is for viewing or listing all the events that the customer has booked'''
        
        return self.db.get_items(queries["GET_BOOKED_EVENTS"], (user_id,))