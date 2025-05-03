const darktoggle = document.getElementById('dark')

darktoggle.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark-theme')
})