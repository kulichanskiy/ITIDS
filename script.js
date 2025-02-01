import { getTime } from "./modules/getTime.js";
import { updateRoute } from "./modules/routeLine.js";
import { blinkTimeColon } from "./modules/blinkingColon.js";


const stations = [
    { id: "station-1", name: "Nanaimo" },
    { id: "station-2", name: "Main Street – Science World" },
    { id: "station-3", name: "Stadium – Chinatown" }
];



let currentStationIndex = 0;

const progressBar = document.querySelector('.progress-bar');
const trainMarker = document.querySelector('.train-marker');
const nextStation = document.getElementById('next-station');
const timeColon = document.getElementById('blinking-colon');
const hours = document.getElementById("current-hour");
const minutesPeriod = document.getElementById("current-minutes-period");

setInterval(() => {
    if (currentStationIndex < stations.length - 1) {
        currentStationIndex++;
        updateRoute(progressBar, trainMarker, nextStation);
    }
}, 1000); 


const blinkingColonUpdate = setInterval(() => {blinkTimeColon(timeColon)}, 2000);
const timeUpdate = setInterval(() => {getTime(hours, minutesPeriod)}, 30000);