import sqlite3
import os

db_path = r'c:\Users\shail\learn_french_site(2)\learn_french_site(2)\learn_french_site\app\learn_french.db'

def inspect():
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    print("Tables:")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    for table in tables:
        print(f" - {table[0]}")
        # Try to count rows and list some titles if it's a story table
        if 'story' in table[0].lower():
            try:
                cur.execute(f"SELECT title FROM {table[0]}")
                titles = cur.fetchall()
                print(f"   Stories in {table[0]}:")
                for title in titles:
                    print(f"     * {title[0]}")
            except Exception as e:
                print(f"   Could not read titles: {e}")
    
    conn.close()

if __name__ == "__main__":
    inspect()
