import sqlite3
import os

db_path = r'c:\Users\shail\learn_french_site(2)\learn_french_site(2)\learn_french_site\app\learn_french.db'

def inspect():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    print("Schema of 'stories':")
    cur.execute("PRAGMA table_info(stories);")
    columns = cur.fetchall()
    for col in columns:
        print(f" - {col[1]} ({col[2]})")
    
    print("\nExisting stories:")
    cur.execute("SELECT id, title FROM stories;")
    for row in cur.fetchall():
        print(f" - ID: {row[0]}, Title: {row[1]}")
    
    conn.close()

if __name__ == "__main__":
    inspect()
