// Scripts for navigation:
//dark-theme


// Highlight current page
const navLinks = document.querySelectorAll(".navigation a"); 
const currentUrl = window.location.pathname;

navLinks.forEach(link => {
    const linkHref = link.getAttribute("href");

    if (linkHref === currentUrl.split("/").pop()) {
    link.classList.add("active");
    }
});



// Footer section scripts
// form validation
document.addEventListener("DOMContentLoaded", () => {
  const contactForm = document.getElementById("contactForm");

  const nameField = document.getElementById("clientName");
  const emailField = document.getElementById("email");
  const phoneField = document.getElementById("phone");
  const messageField = document.getElementById("message");
  const submitButton = document.getElementById("submit-button");

  contactForm.addEventListener("input", () => {
    const allFieldsValid = validateForm();
    submitButton.disabled = !allFieldsValid;
  });

  contactForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Остановить отправку формы

    if (validateForm()) {
      console.log({
        name: nameField.value,
        email: emailField.value,
        phone: phoneField.value,
        message: messageField.value,
      });

      showSuccessMessage("Ваш запрос успешно отправлен!");
      contactForm.reset(); // Очистка формы
      submitButton.disabled = true;
    }
  });

  function validateForm() {
    let isValid = true;

    const namePattern = /^[A-Za-zА-Яа-я\s]+$/;
    if (!nameField.value.trim() || !namePattern.test(nameField.value)) {
      showError(nameField, "Имя должно содержать только буквы.");
      isValid = false;
    } else {
      clearError(nameField);
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailField.value)) {
      showError(emailField, "Введите корректный email.");
      isValid = false;
    } else {
      clearError(emailField);
    }

    const phonePattern = /^\d{10,}$/;
    if (!phonePattern.test(phoneField.value)) {
      showError(phoneField, "Введите номер телефона (минимум 10 цифр).");
      isValid = false;
    } else {
      clearError(phoneField);
    }

    if (messageField.value.trim().length < 20) {
      showError(messageField, "Описание должно содержать минимум 20 символов.");
      isValid = false;
    } else {
      clearError(messageField);
    }

    return isValid;
  }

  function showError(field, message) {
    const errorElement = field.parentElement.querySelector(".error-message");
    if (errorElement) {
      errorElement.innerText = message;
      errorElement.style.color = "red";
    }
  }

  function clearError(field) {
    const errorElement = field.parentElement.querySelector(".error-message");
    if (errorElement) {
      errorElement.innerText = "";
    }
  }

  function showSuccessMessage(message) {
    const existingMessage = document.getElementById("success-message");
    if (existingMessage) existingMessage.remove();

    const successMessage = document.createElement("p");
    successMessage.id = "success-message";
    successMessage.innerText = message;
    successMessage.style.color = "green";
    contactForm.appendChild(successMessage);

    setTimeout(() => successMessage.remove(), 3000);
  }
});
