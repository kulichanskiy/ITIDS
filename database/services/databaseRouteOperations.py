import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
PARENT_DIR = os.path.dirname(BASE_DIR)  

db_path = os.path.join(PARENT_DIR, "itids.db")  

def fetch_route_station_order(route_id): 
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT StationOrder FROM Routes WHERE RouteID = ?", (route_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def fetch_route_destination(route_id): 
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT StationOrder FROM Routes WHERE RouteID = ?", (route_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None
