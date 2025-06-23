// Scripts for navigation:
//dark-theme
(function () {
  const body = document.body;
  const toggleBtn = document.getElementById("dark");

  function setTheme(theme) {
    if (theme === "dark") {
      body.classList.add("dark-theme");
    } else {
      body.classList.remove("dark-theme");
    }
    localStorage.setItem("theme", theme);
  }

  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    body.classList.add("dark-theme");
  }

  if (toggleBtn) {
    toggleBtn.addEventListener("click", () => {
      const isDark = body.classList.contains("dark-theme");
      setTheme(isDark ? "light" : "dark");
    });
  }
})();


// Highlight current page
const navLinks = document.querySelectorAll(".navigation a"); 
const currentUrl = window.location.pathname;

navLinks.forEach(link => {
    const linkHref = link.getAttribute("href");

    if (linkHref === currentUrl.split("/").pop()) {
    link.classList.add("active");
    }
});