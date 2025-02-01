export function blinkTimeColon(colon) {
    colon.classList.add("active");
    setTimeout(() => {
        colon.classList.remove("active");
    }, 1000);   
}