

const stations = [
    { id: "station-1", name: "Nanaimo" },
    { id: "station-2", name: "Main Street – Science World" },
    { id: "station-3", name: "Stadium – Chinatown" }
];

let currentStationIndex = 0;


export function updateRoute(progressBar, trainMarker, nextStation) {
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