// Highlight current page
const navLinks = document.querySelectorAll(".navigation a"); 
const currentUrl = window.location.pathname;
navLinks.forEach(link => {
  const linkHref = link.getAttribute("href");
  if (linkHref === currentUrl.split("/").pop()) {
    link.classList.add("active");
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const contactForm = document.getElementById("contactForm");
  if (contactForm) {
    const nameField = document.getElementById("clientName");
    const emailField = document.getElementById("email");
    const phoneField = document.getElementById("phone");
    const messageField = document.getElementById("message");
    const submitButton = document.getElementById("submit-button");

    // Загрузка сохранённых данных
    const savedData = JSON.parse(localStorage.getItem("contactForm data"));
    if (savedData) {
      nameField.value = savedData.name || "";
      emailField.value = savedData.email || "";
      phoneField.value = savedData.phone || "";
      messageField.value = savedData.message || "";
    }

    // Валидация формы
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

      setTimeout(() => successMessage.remove(), 30000);
    }

    // Сохраняем в localStorage (debounced)
    function debounce(func, delay) {
      let timeout;
      return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => func(...args), delay);
      };
    }

    const saveFormData = debounce(() => {
      const formData = {
        name: nameField.value.trim(),
        email: emailField.value.trim(),
        phone: phoneField.value.trim(),
        message: messageField.value.trim(),
      };
      localStorage.setItem("contactForm data", JSON.stringify(formData));
    }, 1000);

    contactForm.addEventListener("input", () => {
      const allValid = validateForm();
      submitButton.disabled = !allValid;
      saveFormData(); // вызывается debounced
    });

    contactForm.addEventListener("submit", (event) => {
      event.preventDefault();

      if (!validateForm()) return;

      const contactData = {
        name: nameField.value.trim(),
        email: emailField.value.trim(),
        phone: phoneField.value.trim(),
        message: messageField.value.trim(),
      };

      fetch("http://127.0.0.1:8000/api/contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(contactData),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Ошибка отправки запроса");
          }
          return response.json();
        })
        .then((data) => {
          console.log("Ответ сервера:", data);
          showSuccessMessage("Ваш запрос успешно отправлен!");
          contactForm.reset();
          localStorage.removeItem("contactForm data");
          submitButton.disabled = true;
        })
        .catch((error) => {
          console.error("Ошибка:", error);
        });
    });
  }

  // Работа с проектами — проверяем, что элемент есть
  const projectsContainer = document.getElementById('project-container');
  if (projectsContainer) {
    function loadProjects() {
      projectsContainer.innerHTML = "<p>Загрузка проектов...</p>";

      fetch("https://127.0.0.1:8000/api/projects")
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
        projectElement.className = "project-element";
        projectElement.innerHTML = `
            <p class="project-title">${project.title}</p>
            <p class="project-text">${project.description}</p>
            <button class="button">Подробнее...</button>
        `;
        projectsContainer.appendChild(projectElement);
      });
    }

    // Загружаем проекты при загрузке страницы
    window.addEventListener("load", loadProjects);
  }
});
