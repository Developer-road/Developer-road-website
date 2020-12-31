const NavSlide = () => {
    const burger = Document.querySelector('.burger')
    const nav = Document.querySelector('.nav-links')

    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active')
        alert("clicked")
    })
}


const header = () => {
    NavSlide()
}

header()