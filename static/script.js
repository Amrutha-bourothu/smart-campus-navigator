async function loadLocations() {
    const response = await fetch("/locations");
    const locations = await response.json();

    const start = document.getElementById("start");
    const end = document.getElementById("end");

    locations.forEach(location => {
        start.innerHTML += `<option>${location}</option>`;
        end.innerHTML += `<option>${location}</option>`;
    });
}

async function findRoute() {
    const start = document.getElementById("start").value;
    const end = document.getElementById("end").value;

    const response = await fetch(`/route?start=${start}&end=${end}`);
    const data = await response.json();

    document.getElementById("path").innerText =
        "Path: " + data.path.join(" → ");

    document.getElementById("distance").innerText =
        "Distance: " + data.distance + " meters";
}

loadLocations();
