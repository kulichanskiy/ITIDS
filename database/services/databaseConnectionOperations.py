import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
PARENT_DIR = os.path.dirname(BASE_DIR)  

db_path = os.path.join(PARENT_DIR, "itids.db")  

def fetch_connection_row(connection_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT ConnID, LogoLocation, ConnName, BUS_TYPE FROM Connections WHERE ConnID = ?", (connection_id,))
    result = cursor.fetchone()
    conn.close()
    is_bus = result[3] is not None

    if result:
        return {
            "connection_id": result[0],
            "logo_location": result[1],
            "connection_name": result[2],
            "connection_is_bus": is_bus,
            "bus_type": result[3]
        }
    else:
        return None