from flask import Flask, jsonify
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'services'))
print(os.path.join(os.path.dirname(__file__), 'services'))

import databaseRouteOperations
import databaseStationOperations
import databaseConnectionOperations



app = Flask(__name__)

# STATION DATABASE OPERATIONS

@app.route("/get_station_row/<int:station_id>", methods=["GET"])
def get_station_row(station_id):
    station_row = databaseStationOperations.fetch_station_row(station_id)
    if station_row:
        return jsonify(station_row)
    else:
        return jsonify({"error": "Station not found"}), 404

@app.route("/get_station_name/<int:station_id>", methods=["GET"])
def get_station_name_route(station_id):
    name = databaseStationOperations.fetch_station_name(station_id)
    if name:
        return jsonify({"station_name": name})
    else:
        return jsonify({"error": "Station not found"}), 404


# ROUTE DATABASE OPERATIONS

@app.route("/get_route_row/<int:route_id>", methods=["GET"])
def get_route_row(route_id):
    route = databaseRouteOperations.fetch_route_row(route_id)
    if route:
        return jsonify(route)
    else:
        return jsonify({"error": "Cannot define route with ID " + str(route_id) + ". Check database and software for any errors."}), 404

@app.route("/get_route_station_order/<int:route_id>", methods=["GET"])
def get_route_station_order(route_id):
    station_list = databaseRouteOperations.fetch_route_station_order(route_id)
    if station_list:
        return jsonify({"station_order": station_list})
    else:
        return jsonify({"error": "Cannot define Station Order in route with ID " + str(route_id) + ". Check database and software for any errors."}), 404


# CONNECTION DATABASE OPERATIONS

@app.route("/get_connection_row/<int:connection_id>", methods=["GET"])
def get_connection_row(connection_id):
    connection = databaseConnectionOperations.fetch_connection_row(connection_id)
    if connection:
        return jsonify(connection)
    else:
        jsonify({"error": "Cannot define connection with ID " + str(connection_id) + ". Check database and software for any errors."})



if __name__ == "__main__":
    app.run(debug=True)