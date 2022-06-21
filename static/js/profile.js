import data from "/profile/scraping.json" assert { type: "json" };

function loadBadges(items, container_id) {
    let div_container = document.getElementById(container_id);
    items.forEach((item) => {
        console.log(item);
        let badge_tag = document.createElement("div");
        badge_tag.className = "badge rounded-pill mx-1 mb-1";
        badge_tag.innerHTML = `<button type="button" class="btn-close p-1 p1-2 rounded-circle" aria-label="Close"></button>
        <span class="fw-normal" style="font-size: 16px" value="${item}">${item.toUpperCase()}</span>`;
        div_container.appendChild(badge_tag);
    });
}

var keywords = data.queries;
var titles = data.title;
var skills = data.skills;
var categories = data.categories;

loadBadges(keywords, "keyword-badges");
loadBadges(titles, "title-badges");
loadBadges(skills, "skill-badges");
loadBadges(categories, "category-badges");
