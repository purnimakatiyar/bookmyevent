from settings.config import prompts, queries, constants
from models.database import DBConnection
from utils.encrypt import hash_password
from utils.uuid_generator import generate_uuid
from utils import logs


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
       
        
    def signup(self, user_role: str) -> None:
        '''Method for signup in the application for admin and customer'''
        
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
        

    def remove_manager(self, username: str) ->None:
        '''Method for removing the manager by the admin'''
        
        event = self.db.get_item(queries["SEARCH_EXIST_USER_IN_AUTHENTICATE"], (username,))
        if event is None:
            print(prompts["MANAGER_NOT_EXISTS"])
        else:
            self.db.update_item(queries["DELETE_USERDETAILS"], (username,))
            self.db.update_item(queries["DELETE_FROM_AUTHENTICATE"], (username,))
            logs.remove_manager(username)
            print(prompts["REMOVED_MANAGER"])
            
            
    def get_user_id(self, username: str) -> str:
        '''Method for getting user id of the logged in user'''
        
        return self.db.get_item(queries["SEARCH_USER_ID_IN_USERDETAILS"], (username,))[0]
    
    
    CHOICE_TO_QUERY_MAP = {
        constants["ONE"]: queries["UPDATE_PASSWORD"],
        constants["TWO"]: queries["UPDATE_NAME"],
        constants["THREE"]: queries["UPDATE_PHONE"]
    }
    
    
    def update_account(self, choice, new_password = None, new_name=None, new_phone=None)-> None:
        '''Method to update account details for all users'''
        
        if choice in self.CHOICE_TO_QUERY_MAP:
            query = self.CHOICE_TO_QUERY_MAP[choice]
            
        if choice == constants["ONE"]:
            self.db.update_item(query, (hash_password(new_password), self.user_id))
            print(prompts["CHANGED_PASSWORD"])
            
        elif choice == constants["TWO"]:
            self.db.update_item(query, (new_name, self.user_id))
            print(prompts["CHANGED_NAME"])
            
        elif choice == constants["THREE"]:
            self.db.update_item(query, (new_phone, self.user_id))
            print(prompts["CHANGED_PHONE"])
            
        else:
            print(prompts["WRONG_INPUT"])   