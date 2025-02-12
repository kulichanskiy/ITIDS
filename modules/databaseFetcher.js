

// FUNCTIONAL BUT REQUIRES FULL REMAKE

export function ccFetchRoute(routeId) {
    if (!routeId) {
        alert("Enter RouteID!");
        return;
    }

    fetch(`http://127.0.0.1:5000/get_route_row/${routeId}`)
        .then(response => response.json())  
        .then(data => {
            alert(`
                Route ID: ${data.station_id}
                Route Name: ${data.station_name_en}
                `)
        })
        .catch(error => console.log("Error:", error));
}

export function ccFetchStation(stationId) {
    if (!stationId) {
        alert("Enter Station ID!");
        return;
    }

    fetch(`http://127.0.0.1:5000/get_station_row/${stationId}`, {
        method: 'GET',
        mode: 'cors'
    })
        .then(response => response.json()) 
        .then(data => {
            alert(`
                Station ID: ${data.station_id}
                Station Name: ${data.station_name_en}
                Station French Name: ${data.station_name_fr? data.station_name_fr : "-"}
                Zone: ${data.zone}
                Exit directions (Inbound/Outbound): ${data.exit_inbound}/${data.exit_outbound? data.exit_outbound : data.exit_inbound}
                Connections (IDs): ${data.connections.join(', ')}
                `)
        })
        .catch(error => console.log("Error:", error));
}

export function ccFetchConnection(connectionId) {
    if (!connectionId) {
        alert("Enter Connection ID!");
        return;
    }

    fetch(`http://127.0.0.1:5000/get_connection_row/${connectionId}`, {
        method: 'GET',
        mode: 'cors'
    })
        .then(response => response.json()) 
        .then(data => {
            alert(`
                Connection ID: ${data.connection_id}
                Connection Name: ${data.connection_name}
                Bus: ${data.bus_type? "True" : "False"}
                `)
        })
        .catch(error => console.log("Error:", error));
}