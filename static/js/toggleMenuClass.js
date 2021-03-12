// Menú links
const menuLinks = document.getElementById('menuLinks');
const menuIcons = document.getElementById('iconDropDown');
menuIcons.addEventListener('click', () =>
  menuLinks.classList.toggle('ul_dropDownLinks-visible')
);

// Close search bar
const closeSearchBar = document.getElementById('i_search');
closeSearchBar.addEventListener('click', () => console.log('f'));

// Menú profile options
const menu = document.getElementById('navbarDropdownMenuLink');

if (menu) {
  const dropDown = document.getElementById('ulDropDown');
  menu.addEventListener('click', () =>
    dropDown.classList.toggle('ul_dropDown-visible')
  );
}
