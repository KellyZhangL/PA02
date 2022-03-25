import sqlite3

'''
Transaction Class

Stores financial transactions with the fields
'''

class Transaction():
    '''represents a financial transaction'''

    def __init__(self, dbfile):
        connection_obj = sqlite3.connect(dbfile) # connection object
        cursor_obj = connection_obj.cursor() # cursor object
        cursor_obj.execute("DROP TABLE IF EXISTS TRANSACTION")

        table = '''CREATE TABLE TRANSACTION(
            item# int, 
            amount int, 
            category text, 
            date date, 
            description text);'''
        
        connection_obj.commit()
        connection_obj.close()
    
    def __str__(self):
        return "TRANSACTION"

    
    
