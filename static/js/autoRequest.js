function countJobsFound(total_new_entries) {
    // get total job post value
    let results = document.getElementById("jobs-found");

    // Add number of new entries into the previuous total number
    var total = parseInt(results.getAttribute("value")) + total_new_entries;

    // update the innerHTML value with new total
    results.setAttribute("value", total);
    results.innerHTML = total + " Job Posts Found";
}

function autoRequest() {
    // define the XMLHttpRequests function
    const sender = () => {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", "/query", true);
        xhr.onload = function () {
            if (xhr.status == 200) {
                let feed_container = document.querySelector(".feeds");
                let entries = JSON.parse(this.response);
                countJobsFound(entries.length);

                // do for loop on new entries
                entries.reverse().forEach((entry) => {
                    const div = document.createElement("div");
                    let tags = entry.tags.map((tag) => {
                        return '<div class="badge tag text py-2 px-2 my-1 rounded-pill d-inline-block" name="tag">' + tag + "</div>";
                    });
                    tags = tags.join("\n");
                    div.innerHTML = `<p class="text mb-1 fw-semibold green-text" style="font-size: medium">${entry.category}</p>
                    <h5 class="text mb-3"><a target="_blank" id="title" href="${entry.link}">${entry.title}</a><span id='red-asterix' style='color: red'>*</span></h5>
                    <p class="mb-1" id="budget">
                        <span class="fw-semibold">${entry.budget}</span> -
                        <span class="timestamp" id="timestamp" timestamp="${entry.timestamp}">${entry.timestr}</span>
                    </p>
                    <p class="text-break">${entry.description}</p>
                        <div id="tags">
                            ${tags}
                        </div>
                    <p class="text-end my-2"><i class="fa-solid fa-location-dot me-2" style="color: #b7b7b7"></i>${entry.country}</p>
                    <hr/>`;
                    feed_container.insertBefore(div, feed_container.firstChild);
                });
            } else {
                alert("Network Error " + xhr.status);
            }
        };

        xhr.send();
    };
    // set the auto requests interval
    setInterval(sender, 30 * 1e3);
}
autoRequest();
