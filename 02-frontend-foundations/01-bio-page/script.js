let count = 0;

const counterDisplay = document.querySelector("#counter");
const button = document.querySelector("#counter-btn");

button.addEventListener("click", function () {
    count = count + 1;
    counterDisplay.textContent = count;

    if (count === 5) {
        alert("5 projects! You're building real momentum.");
    } else if (count === 10) {
        alert("10 projects — that's a serious portfolio.");
    }
});