import hashlib

def hash_password(password):
        if password is None:
                print("Password cannot be None")
        else:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                return hashed_password

def check_password(password, hashed_password):
        if hash_password(password) == hashed_password:
                return True
        return False