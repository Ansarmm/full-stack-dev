const projectsContainer = document.getElementById("projectsContainer");

function loadProjects() {
    projectsContainer.innerHTML = "<p>Загрузка проектов...</p>";

    fetch("https://jsonplaceholder.typicode.com/posts?_limit=5")
        .then((response) => {
            if (!response.ok) {
                throw new Error("Ошибка загрузки проектов");
            }
            return response.json();
        })
        .then((projects) => {
            displayProjects(projects);
        })
        .catch((error) => {
            projectsContainer.innerText = "Не удалось загрузить проекты.";
            console.error("Ошибка:", error);
        });
}

function displayProjects(projects) {
    projectsContainer.innerHTML = ""; // Очищаем контейнер
    projects.forEach((project) => {
        const projectElement = document.createElement("div");
        projectElement.className = "project";
        projectElement.innerHTML = `
            <h3>${project.id}</h3>
            <h3>${project.title}</h3>
            <p>${project.body}</p>
        `;
        projectsContainer.appendChild(projectElement);
    });
}

// Загружаем проекты при загрузке страницы
window.addEventListener("load", loadProjects);


const addProjectForm = document.getElementById("addProjectForm");

addProjectForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Остановить стандартное поведение формы

    const title = addProjectForm.projectTitle.value.trim();
    const description = addProjectForm.projectDescription.value.trim();

    fetch("https://jsonplaceholder.typicode.com/posts", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, body: description }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Ошибка добавления проекта");
            }
            return response.json();
        })
        .then((newProject) => {
            console.log("Добавлен проект:", newProject);
            loadProjects(); // Перезагружаем список проектов
        })
        .catch((error) => {
            console.error("Ошибка:", error);
        });
});
