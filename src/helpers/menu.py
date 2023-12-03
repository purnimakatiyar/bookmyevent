from helpers.authentication_helper import AuthenticateHelper
from helpers.user_helper import UserHelper
from controllers.event import Event
from helpers.event_helper import EventHelper
from settings.config import constants, menu, prompts
from utils import logs

class Menu:
    
    def navigate_check_role(self, details):
        """Method to check for the role base showing menu for that user"""
        
        if details[1] == constants["ADMIN"]:
            self.admin_menu(details[0])
            return
        elif details[1] == constants["CUSTOMER"]:
            self.customer_menu(details[0]) 
            return
        else:
            self.manager_menu(details[0])
            return
        
    def start_view(self): 
        """Method to show the starting view of the application and menu"""
        
        while True:
            print(menu["START_VIEW"])
            choice = input()
            if choice == constants["ONE"]:
                details = AuthenticateHelper().login()
                if details:
                    self.navigate_check_role(details)    
                else:
                    print(prompts["WRONG_CREDENTIALS"])
                    continue
            elif choice == constants["TWO"]:
                user_role = constants["CUSTOMER"]
                UserHelper().signup(user_role)
            elif choice == constants["THREE"]:
                logs.exit_app()
                break
            else:
                print(prompts["WRONG_INPUT"])
            
    
    def admin_menu(self, username):
        """Method to show the admin menu """
        
        while True:
            print(menu["ADMIN_MENU"])
            choice = input()
            if choice == constants["ONE"]:
                user_role = constants["MANAGER"]
                UserHelper().signup(user_role)
            elif choice == constants["TWO"]:
                UserHelper().remove_manager()
            elif choice == constants["THREE"]:
                self.update_account_menu(username)
            elif choice == constants["FOUR"]:
                self.customer_menu(username)
            elif choice == constants["FIVE"]:
                break
            else:
                print(prompts["WRONG_INPUT"])


    def manager_menu(self, username):
        """Method to show the manager menu"""
        
        while True:
            print(menu["MANAGER_MENU"])
            choice = input()
            if choice == constants["ONE"]:
                EventHelper().add_event(username)
            elif choice == constants["TWO"]:
                EventHelper().remove_event(username)
            elif choice == constants["THREE"]:
                EventHelper().list_events(username)
            elif choice == constants["FOUR"]:
                self.update_event_menu(username)
            elif choice == constants["FIVE"]:
                self.update_account_menu(username)
            elif choice == constants["SIX"]:
                break
            else:
                print(prompts["WRONG_INPUT"])
                

    def update_event_menu(self, username):
        """Method to show the update event menu"""
        
        print(menu["UPDATE_EVENT"])
        while True:
            ch = input()
            if ch in constants.values():
                EventHelper().update_event(username, ch)
                return
            else:
                print(prompts["WRONG_INPUT"])
                print(menu["UPDATE_EVENT"])
                
                
            
    def update_account_menu(self, username):
        """Method to show the update account menu"""
        
        print(menu["UPDATE_ACCOUNT"])
        while True:
            ch = input()
            if ch in constants.values():
                UserHelper().update_account(username, ch)
                return
            else:
                print(prompts["WRONG_INPUT"])
                print(menu["UPDATE_ACCOUNT"])
              
              
    def customer_menu(self, username):
        """Method to show the customer menu"""
        
        while True:
            print(menu["CUSTOMER_MENU"])
            choice = input()
            if choice == constants["ONE"]:
                EventHelper().list_all_events()
            elif choice == constants["TWO"]:
                EventHelper().view_event()
            elif choice == constants["THREE"]:
                EventHelper().book_event(username)
            elif choice == constants["FOUR"]:
                EventHelper().filter_event()
            elif choice == constants["FIVE"]:
                EventHelper().search_event()
            elif choice == constants["SIX"]:
                EventHelper().view_booked_event(username)
            elif choice == constants["SEVEN"]:
                self.update_account_menu(username)
            elif choice == constants["EIGHT"]:
                break
            else:
                print(prompts["WRONG_INPUT"])