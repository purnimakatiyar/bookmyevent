from models.database import DBConnection
from settings.config import queries
import sys
sys.path.append(r'C:\Users\pkatiyar\OneDrive - WatchGuard Technologies Inc\Desktop')

class Authenticate:
    
    def __init__(self, **auth_details) -> None:
        self.username = auth_details.get('username')
        self.password = auth_details.get('password')
        self.db = DBConnection()

    
    def login(self) -> None:
        """Method for the login of user in the application"""
        return self.db.get_item(queries["SEARCH_EXIST_USER_IN_AUTHENTICATE"],(self.username,))
        
        
    def get_role(self) ->str:
        """Method to get the role from the Authentication table"""
        return self.db.get_item(queries["SEARCH_ROLE_IN_AUTHENTICATE"], (self.username,))[0]