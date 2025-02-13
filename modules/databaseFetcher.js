
// FUNCTIONAL 

export function fetchRouteByID(id) {
    if (!id) {
        console.log("Cannot define route id");
        return;
    }

    fetch(`http://127.0.0.1:5000/get_route_row/${id}`)
        .then(response => response.json())  
        .then(data => {
            return data;
        })
        .catch(error => console.log("Error:", error));
}

export function fetchStationByID(id) {
    if (!id) {
        console.log("Cannot define station id");
        return Promise.resolve("Cannot find station with ID "+id);
    }

    return fetch(`http://127.0.0.1:5000/get_station_row/${id}`, {
        method: 'GET',
        mode: 'cors'
    })
        .then(response => response.json()) 
        .then(data => {
            return data;
        })
        .catch(error => console.log("Error:", error));
}

export function fetchConnectionByID(id) {
    if (!id) {
        console.log("Cannot define connection id")
        return;
    }

    fetch(`http://127.0.0.1:5000/get_connection_row/${id}`, {
        method: 'GET',
        mode: 'cors'
    })
        .then(response => response.json()) 
        .then(data => {
            return data;
        })
        .catch(error => console.log("Error:", error));
}