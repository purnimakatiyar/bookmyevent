from controllers.authentication import Authenticate
from settings.config import prompts
from utils.encrypt import check_password
from utils.input import Input
from utils import logs

class AuthenticateHelper:
    
    def login(self):
        auth_details = Input().login_input()
        obj = Authenticate(username = auth_details[0], password = auth_details[1])
        user = obj.login()
        if user is None:
            print(prompts["USERNAME_NOT_EXIST"])
        else:
            stored_hashed_password = user[2]
            if check_password(auth_details[1], stored_hashed_password):
                print(prompts["LOGGED_IN"])
                role = user[3]
                details = (auth_details[0], role)
                return details
            else:
                logs.wrong_credential()
                print(prompts["WRONG_PASSWORD"])
                return None
            
            
            
