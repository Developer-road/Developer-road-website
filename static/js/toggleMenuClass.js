// Menú profile options
const menu = document.getElementById('navbarDropdownMenuLink');
const dropDown = document.getElementById('ulDropDown');
menu.addEventListener('click', () =>
  dropDown.classList.toggle('ul_dropDown-visible')
);

// Menú links
const menuLinks = document.getElementById('menuLinks');
const menuIcons = document.getElementById('iconDropDown');
menuIcons.addEventListener('click', () =>
  menuLinks.classList.toggle('ul_dropDownLinks-visible')
);
