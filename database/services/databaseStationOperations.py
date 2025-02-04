import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
PARENT_DIR = os.path.dirname(BASE_DIR)  
db_path = os.path.join(PARENT_DIR, "itids.db")  

# print("Database loc:", db_path)

def fetch_station_name(station_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT NameEn FROM Stations WHERE StationID = ?", (station_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None
