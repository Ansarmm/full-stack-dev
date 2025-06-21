const requestProjectButton = document.getElementById("requestProjectButton");
const contactForm = document.getElementById("contactForm");
const projectRequestForm = document.getElementById("projectRequestForm");

requestProjectButton.addEventListener("click", () => {
    contactForm.style.display = "none";
    projectRequestForm.style.display = "block";
});

projectRequestForm.addEventListener("input", () => {
    const allFieldsValid = validateForm();
    const submitButton = projectRequestForm.querySelector("button[type='submit']");
    submitButton.disabled = !allFieldsValid;
});

projectRequestForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Остановить отправку формы

    if (validateForm()) {
        console.log({
            name: projectRequestForm.clientName.value,
            email: projectRequestForm.email.value,
            phone: projectRequestForm.phone.value,
            projectType: projectRequestForm.querySelector("input[name='projectType']:checked")?.value || "Не указано",
            message: projectRequestForm.message.value,
        });

        showSuccessMessage("Ваш запрос успешно отправлен!");
        projectRequestForm.reset(); // Очистка формы
        projectRequestForm.querySelector("button[type='submit']").disabled = true;
    }
});

function validateForm() {
    let isValid = true;

    // Имя клиента
    const nameField = projectRequestForm.clientName;
    const namePattern = /^[A-Za-zА-Яа-я\s]+$/;
    if (!nameField.value.trim() || !namePattern.test(nameField.value)) {
        showError(nameField, "Имя должно содержать только буквы.");
        isValid = false;
    } else {
        clearError(nameField);
    }

    // Email
    const emailField = projectRequestForm.email;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailField.value)) {
        showError(emailField, "Введите корректный email.");
        isValid = false;
    } else {
        clearError(emailField);
    }

    // Телефон
    const phoneField = projectRequestForm.phone;
    const phonePattern = /^\d{10,}$/;
    if (!phonePattern.test(phoneField.value)) {
        showError(phoneField, "Введите номер телефона (минимум 10 цифр).");
        isValid = false;
    } else {
        clearError(phoneField);
    }

    // Тип проекта
    const projectType = projectRequestForm.querySelector("input[name='projectType']:checked");
    const projectTypeError = projectRequestForm.querySelector('fieldset .error-message')
    if (!projectType) {
        showError(projectTypeError, `Выберите тип проекта.`);
        isValid = false;
    } else {
        clearError(projectTypeError);
    }

    // Сообщение
    const messageField = projectRequestForm.message;
    if (messageField.value.trim().length < 20) {
        showError(messageField, "Описание должно содержать минимум 20 символов.");
        isValid = false;
    } else {
        clearError(messageField);
    }

    return isValid;
}

function showError(field, message) {
    const errorElement = field.nextElementSibling || field.parentElement.querySelector(".error-message");
    errorElement.innerText = message;
    errorElement.style.color = "red";
}

function clearError(field) {
    const errorElement = field.nextElementSibling || field.parentElement.querySelector(".error-message");
    errorElement.innerText = "";
}

function showSuccessMessage(message) {
    const successMessage = document.createElement("p");
    successMessage.innerText = message;
    successMessage.style.color = "green";
    projectRequestForm.appendChild(successMessage);

    setTimeout(() => successMessage.remove(), 3000);
}