function autoRequest() {
    // define the XMLHttpRequests function
    const sender = () => {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", "/query", true);
        xhr.onload = function () {
            if (xhr.status == 200) {
                let feed = document.getElementById("feed");
                let entries = JSON.parse(this.response);
                let results = document.getElementById("results");
                var total = parseInt(results.getAttribute("value"));
                total += entries.length;
                results.setAttribute("value", total);
                results.innerHTML = total + " Job Posts Found";
                entries.reverse().forEach((entry) => {
                    const hr = document.createElement("hr");
                    const div = document.createElement("div");
                    div.setAttribute("class", "mx-4");
                    feed.insertBefore(hr, feed.firstChild);

                    // define category variable
                    const category = document.createElement("p");
                    category.setAttribute("class", "text mb-1 fw-semibold green-text");
                    category.setAttribute("style", "font-size: medium");
                    category.innerHTML = entry.category;

                    // define title and link variables
                    const title = document.createElement("h5");
                    title.setAttribute("class", "text mb-3");
                    title.innerHTML = "<a target='_blank' href='" + entry.link + "'>" + entry.title + "</a>";

                    // define description variable
                    const description = document.createElement("p");
                    description.setAttribute("class", "text-break");
                    description.innerHTML = entry.description;

                    // define budget, timestamp, and timestr variables
                    const budget = document.createElement("p");
                    const span1 = document.createElement("span");
                    const span2 = document.createElement("span");
                    span1.innerHTML = entry.budget;
                    span1.setAttribute("class", "fw-semibold");
                    span2.innerHTML = entry.timestr;
                    span2.setAttribute("timestamp", entry.timestamp);
                    span2.setAttribute("class", "timestamp");
                    budget.setAttribute("class", "mb-1");
                    budget.setAttribute("style", "font-size: 14px; color: gray");
                    budget.append(span1, " - ", span2);

                    // define country variable
                    const country = document.createElement("p");
                    country.setAttribute("class", "text-end my-2");
                    country.innerHTML = '<i class="fa-solid fa-location-dot me-2" style="color: #b7b7b7"></i>' + entry.country;

                    // append childs
                    div.append(category, title, budget, description);

                    // define tags variable
                    const tags = entry.tags;
                    tags.forEach((value) => {
                        const tag = document.createElement("div");
                        tag.setAttribute("class", "text py-1 px-2 my-1 rounded-pill d-inline-block");
                        tag.setAttribute("id", "tags");
                        tag.innerHTML = value;
                        div.append(tag, " ");
                    });

                    // append childs
                    div.append(country);

                    // insert new div to top
                    feed.insertBefore(div, feed.firstChild);
                    feed.insertBefore(hr, feed.firstChild);
                });
            } else {
                alert("Network Error " + xhr.status);
            }
        };

        xhr.send();
    };
    // set the auto requests interval
    setInterval(sender, 60 * 1e3);
}
autoRequest();
