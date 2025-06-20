alert("Добро пожаловать в мой портфолио")


const darktoggle = document.getElementById('dark')

darktoggle.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark-theme')
})