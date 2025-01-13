// Станции маршрута
const stations = [
    { id: "station-1", name: "Nanaimo" },
    { id: "station-2", name: "Main Street – Science World" },
    { id: "station-3", name: "Stadium – Chinatown" }
];

let currentStationIndex = 0;

const progressBar = document.querySelector('.progress-bar');
const trainMarker = document.querySelector('.train-marker');
const nextStation = document.getElementById('next-station');

// Функция обновления линии маршрута
function updateRoute() {
    const progressPercentage = (currentStationIndex / (stations.length - 1)) * 100;

    progressBar.style.width = `${progressPercentage}%`;
    trainMarker.style.left = `${progressPercentage}%`;

    // Обновляем активную станцию
    stations.forEach((station, index) => {
        const stationElement = document.getElementById(station.id);
        if (index <= currentStationIndex) {
            stationElement.classList.add('active');
        } else {
            stationElement.classList.remove('active');
        }
    });

    // Обновляем текст следующей станции
    nextStation.textContent = stations[currentStationIndex + 1]?.name || "End of Line";
}

// Автоматическое движение по маршруту (пример)
setInterval(() => {
    if (currentStationIndex < stations.length - 1) {
        currentStationIndex++;
        updateRoute();
    }
}, 3000); // Каждые 3 секунды
