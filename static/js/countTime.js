function countTime() {
    // define time to str function
    function time2str(seconds) {
        const hours = Math.floor(seconds / 3600);
        const minutes = Math.round((seconds % 3600) / 60);
        if (hours == 0.0) {
            return minutes + "m ago";
        } else {
            return hours + "h " + minutes + "m ago";
        }
    }
    // define current timestamp
    const now = new Date().getTime() / 1e3;

    // get all tag with timestamp class name
    const spans = document.getElementsByClassName("timestamp");
    for (let i = 0; i < spans.length; i++) {
        const timestamp = spans[i].getAttribute("timestamp");
        const gap = new Date(now - timestamp);
        spans[i].innerHTML = time2str(gap);
    }
}
setInterval(countTime, 60 * 1e3);