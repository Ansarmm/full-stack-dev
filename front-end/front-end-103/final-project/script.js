// Scripts for navigation:
//dark-theme
const darktoggle = document.getElementById('dark')

darktoggle.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark-theme')
})

// Highlight current page
const navLinks = document.querySelectorAll(".navigation a"); 
const currentUrl = window.location.pathname;

navLinks.forEach(link => {
    const linkHref = link.getAttribute("href");

    if (linkHref === currentUrl.split("/").pop()) {
    link.classList.add("active");
    }
});