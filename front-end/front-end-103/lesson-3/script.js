const aboutText = document.getElementById("aboutText");
const updateButton = document.getElementById("updateAbout");

updateButton.addEventListener("click", () => {
    aboutText.innerText = "Это обновлённое описание, созданное с помощью JavaScript!";
});

const aboutHeading = document.getElementById("aboutHeading");
aboutHeading.style.color = "green";
aboutHeading.style.fontSize = "32px";

const button = document.querySelector("#updateAbout");
button.innerText = "Кликни меня!";