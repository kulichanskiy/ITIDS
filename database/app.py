from flask import Flask, jsonify
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'services'))

print(os.path.join(os.path.dirname(__file__), 'services'))

from databaseRouteOperations import fetch_route_station_order
from databaseStationOperations import fetch_station_name


app = Flask(__name__)

@app.route("/get_station_name/<int:station_id>", methods=["GET"])
def get_station_name_route(station_id):
    name = fetch_station_name(station_id)
    if name:
        return jsonify({"station_name": name})
    else:
        return jsonify({"error": "Station not found"}), 404


@app.route("/get_route_station_order/<int:route_id>", methods=["GET"])
def get_route_station_order(route_id):
    station_list = fetch_route_station_order(route_id)
    if station_list:
        return jsonify({"station_order": station_list})
    else:
        return jsonify({"error": "Cannot define Station Order in route with ID " + str(route_id) + ". Check database and software for any errors."}), 404


if __name__ == "__main__":
    app.run(debug=True)