import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
PARENT_DIR = os.path.dirname(BASE_DIR)  

db_path = os.path.join(PARENT_DIR, "itids.db")  

def fetch_route_row(station_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT RouteID, RouteName, LogoLocation, DestStation FROM Routes WHERE RouteID = ?", (station_id,))
    result = cursor.fetchone()
    cursor.execute("SELECT StationOrder FROM Routes WHERE RouteID = ?", (station_id,))
    stn_order = cursor.fetchone()
    conn.close()

    station_order_str = stn_order[0].split()
    station_order_ids = [int(id) for id in station_order_str]

    if result:
        return {
            "route_id": result[0],
            "route_name": result[1],
            "logo_location": result[2],
            "destination_id": result[3],
            "station_order_ids": station_order_ids
        }
    else:
        return None

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
