
function fetchRoute() {
    let routeId = document.getElementById("routeId").value;
    if (!routeId) {
        alert("Введите RouteID!");
        return;
    }

    fetch(`http://127.0.0.1:5000/get_route_row/${routeId}`)
        .then(response => response.json())  // Парсим JSON
        .then(data => {
            if (data.error) {
                document.getElementById("routeName").innerText = "Маршрут не найден";
                document.getElementById("busType").innerText = "";
            } else {
                document.getElementById("routeName").innerText = data.route_name;
                document.getElementById("busType").innerText = data.has_bus_type ? "Есть" : "Нет"; // ✅ Проверяем булевое значение
            }
        })
        .catch(error => console.log("Ошибка:", error));
}

function fetchStation() {
    let routeId = document.getElementById("routeId").value;
    if (!routeId) {
        alert("Введите RouteID!");
        return;
    }

    fetch(`http://127.0.0.1:5000/get_route_row/${routeId}`)
        .then(response => response.json())  // Парсим JSON
        .then(data => {
            if (data.error) {
                document.getElementById("routeName").innerText = "Маршрут не найден";
                document.getElementById("busType").innerText = "";
            } else {
                document.getElementById("routeName").innerText = data.route_name;
                document.getElementById("busType").innerText = data.has_bus_type ? "Есть" : "Нет"; // ✅ Проверяем булевое значение
            }
        })
        .catch(error => console.log("Ошибка:", error));
}