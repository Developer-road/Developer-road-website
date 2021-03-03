const toggleMenuClass = () => {
    const menu = document.getElementById('mobile-menu');
    menu.addEventListener('click', () => menu.classList.toggle('menu-open'));
}
