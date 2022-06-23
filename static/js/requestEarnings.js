const getEarnings = () => {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "/get-earnings", true);
    xhr.onload = function () {
        if (xhr.status == 200) {
            let entries = JSON.parse(this.response);
            let earning_usd = document.getElementById("usd");
            let earning_idr = document.getElementById("idr");
            let usd_idr = document.getElementById("usd_idr_rate");
            let avail_date = document.getElementById("avail_date");
            earning_usd.innerHTML = entries["value_usd"];
            earning_idr.innerHTML = entries["value_idr"];
            usd_idr.innerHTML = entries["usd_idr"];
            avail_date.innerHTML = entries["avail_date"];
        }
    };
    xhr.send();
};

// run the function at startup
getEarnings();
