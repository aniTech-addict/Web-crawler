import sqlite3

class Database_Manager:
    def __init__(self,db_name):
        self.db_name = db_name
        self.init_db()
        
    def connect(self):
        return sqlite3.connect(self.db_name)
    
    def init_db(self):
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE IF NOT EXISTS ? 
            id INTEGER PRIMARY KEY AUTOINCREMENT
            heading TEXT
            description TEXT
        ''',(self.db_name))
    
    
        
        conn.commit()
        conn.close()
         
        
                
        