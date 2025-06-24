import sqlite3

class DatabaseManager:
    def __init__(self, db_name_file): # Renamed for clarity, this is the DB file
        self.db_name_file = db_name_file
        self.table_name = "crawled_pages" # Define your table name
        self.init_db()
        
    def connect(self):
        return sqlite3.connect(self.db_name_file)
    
    def init_db(self):
        conn = self.connect()
        cursor = conn.cursor()
        
        # Table and column names cannot be parameterized in CREATE TABLE.
        # Use string formatting carefully.
        # Ensure self.table_name is a safe, hardcoded, or sanitized string.
        create_table_sql = f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE, 
                title TEXT,
                retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        '''
        # Example: Adding a URL, title, and timestamp
        # You'd likely have separate methods to add data.
        
        cursor.execute(create_table_sql)
            
        conn.commit()
        conn.close()

    def add_crawled_page(self, url, title):
        conn = self.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f'''
                INSERT INTO {self.table_name} (url, title)
                VALUES (?, ?)
            ''', (url, title))
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"URL {url} already exists in the database.") # Or handle as needed
        finally:
            conn.close()
            
def main():
    print('~~~~~~~~~~~~~~~~~ATTENTION~~~~~~~~~~~~~~~~~')
    print("This file is not to be ran directly.")
    input()

if __name__ == "__main__":
    main()
