import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
PARENT_DIR = os.path.dirname(BASE_DIR)  
db_path = os.path.join(PARENT_DIR, "itids.db")  

# print("Database loc:", db_path)

def fetch_station_row(station_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT StationID, NameEn, NameFr, Zone, Connects FROM Stations WHERE StationID = ?", (station_id,))
    result = cursor.fetchone()
    cursor.execute("SELECT ConnectionID FROM StationConnections WHERE StationID = ?", (station_id,))
    connections_id = cursor.fetchall()
    conn.close()
    if result:
        return {
            "station_id": result[0],
            "station_name_en": result[1],
            "station_name_fr": result[2],
            "zone": result[3],
            "connections": [connections_id[0] for connections_id in connections_id]
        }
    else:
        return None

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
