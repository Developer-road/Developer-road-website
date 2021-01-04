const main = () => {

    const menu = document.getElementById('mobile-menu');
    const menuLinks = document.querySelector('.my-nav-menu')
    
    menu.addEventListener('click', () =>{
            menu.classList.toggle('is-active')
            menuLinks.classList.toggle('active')
    });
}


main()