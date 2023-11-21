from bcrypt import checkpw, hashpw, gensalt


def check_password(password, hashed_password):
        if checkpw(password.encode('utf8'), hashed_password):
            return True
        return False
    
def hash_password(password):
        salt = gensalt()
        hashed_password = hashpw(password.encode('utf-8'), salt)
        return hashed_password