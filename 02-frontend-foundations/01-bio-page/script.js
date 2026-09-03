let count = 0;

const counterDisplay = document.querySelector("#counter");
const button = document.querySelector("#counter-btn");
const projects = ["Calculator", "Budget Tracker", "AI Study Buddy", "Bio Page"];
const input = document.querySelector("#new-project-input");
const addButton = document.querySelector("#add-project-btn");

const projectList = document.querySelector("#project-list");

projects.forEach(function (project) {
    const li = document.createElement("li");
    li.textContent = project;
    projectList.appendChild(li);
});

addButton.addEventListener("click", function () {
    const newProject = input.value;

    if (newProject === "") {
        alert("Please type something first!");
        return;
    }

    const li = document.createElement("li");
    li.textContent = newProject;
    projectList.appendChild(li);
    input.value = "";
});

button.addEventListener("click", function () {
    count = count + 1;
    counterDisplay.textContent = count;
    

    if (count === 5) {
        alert("5 projects! You're building real momentum.");
    } else if (count === 10) {
        alert("10 projects — that's a serious portfolio.");
    }
});