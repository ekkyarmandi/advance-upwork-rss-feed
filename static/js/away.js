var prevResults;
var alertInterval;
var myInterval;
var activated = false;

function notify() {
    let alert = false;
    let title = "UpWork RSS Feed | Ekky Armandi";
    let currentResults = document.getElementById("results").getAttribute("value");
    let count = currentResults - prevResults;
    alertInterval = setInterval(() => {
        document.title = alert ? title : "(" + count + ") New Jobs Post | " + title;
        alert = !alert;
    }, 1000);
}

window.onfocus = () => {
    // define the prevResults to 0
    prevResults = 0;
    activated = false;
    clearInterval(alertInterval);
    document.title = "UpWork RSS Feed | Ekky Armandi";
};

window.onblur = () => {
    // define the prevResults as value from results id
    prevResults = document.getElementById("results").getAttribute("value");
    prevResults = parseInt(prevResults);
};

myInterval = setInterval(() => {
    let currentResults = document.getElementById("results").getAttribute("value");
    currentResults = parseInt(currentResults);
    // console.log("Now: " + currentResults + ", Before: " + prevResults);
    if ((currentResults > prevResults) & (prevResults > 0) & !activated) {
        activated = true;
        notify();
    }
}, 60 * 1e3);
