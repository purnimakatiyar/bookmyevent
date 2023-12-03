from settings.config import prompts, constants
from utils.input import Input
from controllers.user import User
from utils import logs

class UserHelper:
    
    def signup(self, user_role):
        """Method to do the signup process for a user"""
        
        signup_details = Input().signup_input()
        user = User(
        username = signup_details[0],
        password = signup_details[1],
        name = signup_details[2],
        phone = signup_details[3],
        role = user_role
        )
        
        if user.signup():
            print(prompts["USERNAME_EXISTS"])
        else:
            user.save_info()
            print(prompts["USER_ADDED"])
            
    def remove_manager(self):
        """Method to remove the manager"""
        
        username = Input().remove_manager_input()
        user = User().get_user(username)
        if user is None:
            print(prompts["MANAGER_NOT_EXISTS"])
        else:
            User().remove_manager(username)
            logs.remove_manager(username)
            print(prompts["REMOVED_MANAGER"])
            
            
    def update_account(self, username, choice):
        """Method to update the account"""
        
        user = User(user_id = User().get_user_id(username),)
        update_acc_details = Input().update_account_input(choice)
        
        if user.update_account(update_acc_details[0], update_acc_details[1], update_acc_details[2], update_acc_details[3]):
            if choice == constants["ONE"]:
                print(prompts["CHANGED_PASSWORD"])
            elif choice == constants["TWO"]:
                print(prompts["CHANGED_NAME"])
            elif choice == constants["THREE"]:
                print(prompts["CHANGED_PHONE"])