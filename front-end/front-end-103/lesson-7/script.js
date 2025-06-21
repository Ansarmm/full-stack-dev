const requestProjectButton = document.getElementById("requestProjectButton");
const contactForm = document.getElementById("contactForm");
const projectRequestForm = document.getElementById("projectRequestForm");

requestProjectButton.addEventListener("click", () => {
    contactForm.style.display = "none";
    projectRequestForm.style.display = "block";
});

projectRequestForm.addEventListener("input", () => {
    const formData =  {
            name: projectRequestForm.clientName.value,
            email: projectRequestForm.email.value,
            phone: projectRequestForm.phone.value,
            projectType: projectRequestForm.querySelector("input[name='projectType']:checked")?.value || "Не указано",
            message: projectRequestForm.message.value,
        };
        localStorage.setItem("projectRequestData", JSON.stringify(formData));
});

window.addEventListener("load", () => {
    const savedData = JSON.parse(localStorage.getItem("projectRequestData"));

    if (savedData) {
        projectRequestForm.clientName.value = savedData.name || "";
        projectRequestForm.email.value = savedData.email || "";
        projectRequestForm.phone.value = savedData.phone || "";

        if (savedData.projectType) {
            const projectTypeInput = projectRequestForm.querySelector(`input[name='projectType'][value='${savedData.projectType}']`);
            if (projectTypeInput) projectTypeInput.checked = true;
        }

        projectRequestForm.message.value = savedData.message || "";
    }
});

projectRequestForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Остановить стандартное поведение формы
    isClicked = true

    if (isClicked) { // Я понимаю что это неправильно, это для тестирования
        console.log("Форма успешно отправлена!");
        localStorage.removeItem("projectRequestData"); // Удаляем данные из localStorage
        projectRequestForm.reset(); // Очищаем форму
    }
});

const clearButton = document.createElement("button");
clearButton.innerText = "Очистить форму";
clearButton.type = "button"; // Не отправляет форму
projectRequestForm.appendChild(clearButton);

clearButton.addEventListener("click", () => {
    projectRequestForm.reset();
    localStorage.removeItem("projectRequestData");
    console.log("Форма и данные успешно очищены.");
});


function debounce(func, delay) {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => func(...args), delay);
    };
}

const saveFormData = debounce(() => {
    const formData = {
        name: projectRequestForm.clientName.value,
        email: projectRequestForm.email.value,
        phone: projectRequestForm.phone.value,
        projectType: projectRequestForm.querySelector("input[name='projectType']:checked")?.value || "",
        message: projectRequestForm.message.value,
    };

    localStorage.setItem("projectRequestData", JSON.stringify(formData));
}, 500);

projectRequestForm.addEventListener("input", saveFormData);