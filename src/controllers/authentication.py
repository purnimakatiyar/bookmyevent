from models.database import DBConnection
from settings.config import queries, prompts
from utils.encrypt import check_password
import sys
sys.path.append(r'C:\Users\pkatiyar\OneDrive - WatchGuard Technologies Inc\Desktop')

class Authenticate:
    
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password
        self.db = DBConnection()

    
    def login(self):
        check_user = self.db.get_item(queries["SEARCH_EXIST_USER_IN_AUTHENTICATE"],(self.username,))
        if check_user is None:
            print(prompts["USERNAME_NOT_EXIST"])
        else:
            stored_hashed_password = check_user[2]
            if check_password(self.password, stored_hashed_password):
                print(prompts["LOGGED_IN"])
                return self.get_role()
            else:
                print(prompts["WRONG_PASSWORD"])
                return None

    def get_role(self):
        return self.db.get_item(queries["SEARCH_ROLE_IN_AUTHENTICATE"], (self.username,))[0]