from settings.config import prompts, queries
from models.database import DBConnection
from utils.encrypt import hash_password
from helpers.uuid_generator import generate_uuid



class User:
    
    
    def __init__(self, **user_details):
        self.uuid = generate_uuid()
        self.username = user_details.get('username')
        self.password = user_details.get('password')
        self.name = user_details.get('name')
        self.phone = user_details.get('phone')
        self.role = user_details.get('role')
        self.db = DBConnection()
       
        
    def signup(self, user_role):
        check_user = self.db.get_item(queries["SEARCH_EXIST_USER_IN_AUTHENTICATE"], (self.username,))
        if check_user:
            print(prompts["USERNAME_EXISTS"])
        else:
            hashed_password = hash_password(self.password)
            auth_details = (
                self.uuid,
                self.username,
                hashed_password,
                user_role
            )
            user_details = (
                self.uuid,
                self.username, 
                self.name,
                self.phone,
            )
            self.db.insert_item(queries["INSERT_INTO_AUTHENTICATE"], auth_details) 
            self.db.insert_item(queries["INSERT_USERDETAILS"], user_details)
            print(prompts["USER_ADDED"])
        

    def remove_manager(self, username):
        event = self.db.get_item(queries["SEARCH_EXIST_USER_IN_AUTHENTICATE"], (username,))
        if event is None:
            print(prompts["MANAGER_NOT_EXISTS"])
        else:
            self.db.update_item(queries["DELETE_USERDETAILS"], (username,))
            self.db.update_item(queries["DELETE_FROM_AUTHENTICATE"], (username,))
            print(prompts["REMOVED_MANAGER"])
            
    def get_user_id(self, username):
        return self.db.get_item(queries["SEARCH_USER_ID_IN_USERDETAILS"], (username,))[0]