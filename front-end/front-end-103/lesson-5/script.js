const projectContainer = document.getElementById('project-container')
const addProjectButton = document.querySelector('.add-projectBtn')
const deleteProjectsButton = document.querySelector('.delete-projectsBtn')

let projectCount = 0

addProjectButton.addEventListener('click', () => {
    projectCount++;

    const projectCard = document.createElement('div')  

    projectCard.className = 'project-card'
    projectCard.innerHTML =
        `<h3>Заголовок ${projectCount}</h3>
        <p>Описание ${projectCount}</p>
        <button class='delete-project'>Удалить</button>`;

    projectContainer.appendChild(projectCard)

    if (document.getElementById("emptyMessage")) {
        document.getElementById("emptyMessage").remove();
    }
})

projectContainer.addEventListener("click", (event) => {
    if (event.target.classList.contains("delete-project")) {
        event.target.parentElement.remove();
    }
});

deleteProjectsButton.addEventListener('click', () => {
    projectContainer.innerHTML = ''
    projectCount = 0
})

if (projectContainer.children.length === 0) {
    const emptyMessage = document.createElement("p");
    emptyMessage.id = "emptyMessage";
    emptyMessage.innerText = "Проектов пока нет. Нажмите 'Добавить проект', чтобы создать новый.";
    projectContainer.appendChild(emptyMessage);
}
