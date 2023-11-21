from helpers.input import Input
from controllers.event import Event
from settings.config import constants, menu, prompts


class Menu:
    
    def navigate_check_role(self, details):
        if details[1] == constants["ADMIN"]:
            self.admin_menu()
            return
        elif details[1] == constants["CUSTOMER"]:
            self.customer_menu(details[0]) 
            return
        else:
            self.manager_menu(details[0])
            return
        
    def start_view(self): 
        while True:
            print(menu["START_VIEW"])
            choice = input()
            if choice == constants["ONE"]:
                details = Input().login_input()
                if details:
                    self.navigate_check_role(details)    
                else:
                    print(prompts["WRONG_CREDENTIALS"])
                    continue
            elif choice == constants["TWO"]:
                user_role = constants["CUSTOMER"]
                Input().signup_input(user_role)
            elif choice == constants["THREE"]:
                break
            else:
                print(prompts["WRONG_INPUT"])
            
    
    def admin_menu(self):
        while True:
            print(menu["ADMIN_MENU"])
            choice = input()
            if choice == constants["ONE"]:
                user_role = constants["MANAGER"]
                Input().signup_input(user_role)
            elif choice == constants["TWO"]:
                Input().remove_manager_input()
            elif choice == constants["THREE"]:
                break
            else:
                print(prompts["WRONG_INPUT"])


    def manager_menu(self, username):
        while True:
            print(menu["MANAGER_MENU"])
            choice = input()
            if choice == constants["ONE"]:
                Input().add_event_input(username)
            elif choice == constants["TWO"]:
                Input().remove_event_input(username)
            elif choice == constants["THREE"]:
                Input().list_event_input(username)
            elif choice == constants["FOUR"]:
                self.update_event_menu(username)
            elif choice == constants["FIVE"]:
                break
            else:
                print(prompts["WRONG_INPUT"])
                

    def update_event_menu(self, user):
        print(menu["UPDATE_EVENT"])
        ch = input()
        if ch in constants.values():
            Input().update_event_input(user, ch)
        else:
            print(prompts["WRONG_INPUT"])

              
    def customer_menu(self, username):
        while True:
            print(menu["CUSTOMER_MENU"])
            choice = input()
            if choice == constants["ONE"]:
                Event().list_all_events()
            elif choice == constants["TWO"]:
                Input().view_event_input()
            elif choice == constants["THREE"]:
                Input().book_event_input(username)
            elif choice == constants["FOUR"]:
                Input().filter_event_input()
            elif choice == constants["FIVE"]:
                Input().search_event_input()
            elif choice == constants["SIX"]:
                Input().view_booked_event_input(username)
            elif choice == constants["SEVEN"]:
                break
            else:
                print(prompts["WRONG_INPUT"])