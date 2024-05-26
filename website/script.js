const table = document.querySelector("table");
const header = document.querySelector("header");
const file = "../json/output.json";
const [slider, input] = document.querySelectorAll("input");
let seats = slider.value;
const perc = document.querySelector("#percentage");
let data;

async function fetchData() {
    const res = await fetch(file);
    data = await res.json();
    updateTable();
}

fetchData();

function getRandomColor() {
    var letters = 'BCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * letters.length)];
    }
    return color;
}

function updateTable() {
    table.innerHTML = "";
    perc.innerHTML = "";

    let backendTable = [];
    let totalVotes = data.reduce((total, e) => total + e.votes, 0);
    let worth = totalVotes / seats;
    let tr;

    data.forEach(e => {
        const party = e.party;
        const seatsWon = Math.round(e.votes / worth);
        let color = getRandomColor();
        for (let i = 0; i <= seatsWon; i++) {
            backendTable.push({ "party": party, "color": color, "seatswon": seatsWon });
        }
    });

    perc.innerHTML = `${Math.floor((worth / totalVotes) * 10000) / 100}%`;

    for (let i = 0; i < seats; i++) {
        const td = document.createElement("td");
        td.appendChild(document.createTextNode(backendTable[i].party || "empty seat"));
        td.style.backgroundColor = backendTable[i].color;
        if (i == 0 || i % 10 == 0) {
            tr = document.createElement("tr");
        }
        tr.appendChild(td);
        table.appendChild(tr);
    };
}

slider.addEventListener("input", () => {
    input.value = slider.value;
    seats = slider.value;
    updateTable();
});

input.addEventListener("input", () => {
    slider.value = input.value;
    seats = input.value;
    updateTable();
});