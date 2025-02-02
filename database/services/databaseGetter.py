from flask import Flask, jsonify
import sqlite3

# conn = sqlite3.connect("database/itids.db")
# cursor = conn.cursor()

app = Flask(__name__)


def get_station_name(station_id):
    conn = sqlite3.connect("../itids.db")
    cursor = conn.cursor()
    cursor.execute("SELECT NameEn FROM Stations WHERE StationID = ?", (station_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        print(result[0])
        return result[0]
    else:
        print("Hiuta")
        return None
    

@app.route("/get_station_name/<int:station_id>", methods=["GET"])
def get_station_name_route(station_id):
    name = get_station_name(station_id)
    if name:
        return jsonify({"station_name": name})
    else:
        return jsonify({"error": "Station not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)