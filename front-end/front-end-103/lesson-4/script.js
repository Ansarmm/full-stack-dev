const contactForm = document.getElementById("contactForm");
const formFeedback = document.getElementById("formFeedback");

contactForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Остановить стандартное поведение формы

    // Получение значений полей
    const name = contactForm.name.value.trim();
    const email = contactForm.email.value.trim();
    const message = contactForm.message.value.trim();

    // Проверка полей
    if (name && email && message) {
        formFeedback.style.display = "block";
        formFeedback.style.color = "green";
        formFeedback.innerText = "Форма успешно отправлена! Спасибо за ваше сообщение.";
        contactForm.reset(); // Очистить поля формы
        
        console.log("Имя:", name);
        console.log("Email:", email);
        console.log("Сообщение:", message);
    } else {
        formFeedback.style.display = "block";
        formFeedback.style.color = "red";
        formFeedback.innerText = "Пожалуйста, заполните все поля.";
    }
});