
// For demonstration, this module uses computer time ranges, based on time you set on settings. 
// To integrate this module to subway system, rewrite this module.


export function getTime(hourSpan, minutesPeriodSpan) {

    if (!hourSpan || !minutesPeriodSpan) {
        console.error("Time error. Cannot update.");
        return;
    }

    const currentDate = new Date();
    let hours = currentDate.getHours();
    const minutes = currentDate.getMinutes();

    const period = hours >= 12 ? "PM" : "AM";
    const formattedMinutes = minutes < 10 ? "0" + minutes : minutes;

    hours = hours % 12;
    hours = hours ? hours : 12;

    hourSpan.textContent = hours;
    minutesPeriodSpan.textContent = formattedMinutes + period;

    console.log(`Time updated: ${hours}:${formattedMinutes} ${period}`);
}