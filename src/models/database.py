from settings import config
import sqlite3


class DBConnection:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
            cls._instance.host = config.constants["BOOKMYEVENT_DB"]
            cls._instance.cursor = None

        return cls._instance

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        self.cursor = self.connection.cursor()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Exception traceback: {exc_tb}")

        else:
            self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()     
            
    
    def get_item(self, query, data):
        response = None
        with db as cursor:
            try:
                response = cursor.execute(query, data).fetchone()
            except sqlite3.Error as error:
                print(error)
            return response
    
    
    def get_items(self, query, data):
        response = None
        with db as cursor:
            try:
                response = cursor.execute(query, data).fetchall()
            except sqlite3.Error as error:
                print(error)
            return response
        
    
    def get_all_events(self, query):
        events = None
        with self as cursor:
            try:
                events = cursor.execute(query).fetchall()
            except sqlite3.Error as error:
                print(error)
            return events

    # def get_events(self, query, data):
    #     response = None
    #     with self as cursor:
    #         try:
    #             response = cursor.execute(query, data).fetchall()
    #         except sqlite3.Error as error:
    #             print(error)
    #     return response
    
    
    def insert_item(self, query, data):
        with db as cursor:
            try:
                cursor.execute(query, data)
            except sqlite3.Error as error:
                print(error)

    
    def update_item(self, query, data):
        with db as cursor:
            try:
                cursor.execute(query, data)
            except sqlite3.Error as error:
                print(error)
             
         
    def delete_item(self, query, data):
        with db as cursor:
            try:
                cursor.execute(query, data)
            except sqlite3.Error as error:
                print(error)
            

db = DBConnection()