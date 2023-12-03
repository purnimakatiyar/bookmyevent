from settings.config import queries, constants
from models.database import DBConnection
from utils.encrypt import hash_password
from utils.uuid_generator import generate_uuid


class User:
    
    
    def __init__(self, **user_details: dict) ->None:
        self.uuid = generate_uuid()
        self.user_id = user_details.get('user_id')
        self.username = user_details.get('username')
        self.password = user_details.get('password')
        self.name = user_details.get('name')
        self.phone = user_details.get('phone')
        self.role = user_details.get('role')
        self.db = DBConnection()
       
        
    def signup(self) -> None:
        '''Method for signup in the application for admin and customer'''
        
        return self.db.get_item(queries["SEARCH_EXIST_USER_IN_AUTHENTICATE"], (self.username,))

            
    def save_info(self):
        '''Method to save the user details into database'''
        
        hashed_password = hash_password(self.password)
        auth_details = (
            self.uuid,
            self.username,
            hashed_password,
            self.role
            )
        user_details = (
            self.uuid,
            self.username, 
            self.name,
            self.phone,
            )
        self.db.insert_item(queries["INSERT_INTO_AUTHENTICATE"], auth_details)
        self.db.insert_item(queries["INSERT_USERDETAILS"], user_details)
        return
        
            
    def get_user(self, username):
        '''Method to get existing user in the database'''
        
        return self.db.get_item(queries["SEARCH_EXIST_USER_IN_AUTHENTICATE"], (username,))
    
    def remove_manager(self, username: str) ->None:
        '''Method for removing the manager by the admin'''
        
        self.db.update_item(queries["DELETE_USERDETAILS"], (username,))
        self.db.update_item(queries["DELETE_FROM_AUTHENTICATE"], (username,))
        
            
            
    def get_user_id(self, username: str) -> str:
        '''Method for getting user id of the logged in user'''
        
        return self.db.get_item(queries["SEARCH_USER_ID_IN_USERDETAILS"], (username,))[0]
    
  
    
    def update_account(self, choice, new_password = None, new_name=None, new_phone=None)-> None:
        '''Method to update account details for all users'''
        
        if choice == constants["ONE"]:
            password = hash_password(new_password)
            self.db.update_item(queries["UPDATE_PASSWORD"], (password, self.user_id))
            return True
        elif choice == constants["TWO"]:
            self.db.update_item(queries["UPDATE_NAME"], (new_name, self.user_id))
            return True
        elif choice == constants["THREE"]:
            self.db.update_item(queries["UPDATE_PHONE"], (new_phone, self.user_id))
            return True