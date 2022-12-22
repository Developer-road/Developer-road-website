// Menú links
const menuLinks = document.getElementById('menuLinks');
const menuIcons = document.getElementById('iconDropDown');
menuIcons.addEventListener('click', () =>
  menuLinks.classList.toggle('ul_dropDownLinks-visible')
);

// Open search bar
const searchBar = document.getElementById('div_showSearchBar');

// Search icon 
const openSearchBar = document.getElementById('a_search');
openSearchBar.addEventListener('click', () =>
  searchBar.classList.add('div__searchBar')
);

// Close search bar
const closeSearchBar = document.getElementById('a_searchClose');
closeSearchBar.addEventListener('click', () =>
  searchBar.classList.remove('div__searchBar')
);

// Menú profile options
const menu = document.getElementById('navbarDropdownMenuLink');

if (menu) {
  const dropDown = document.getElementById('ulDropDown');
  menu.addEventListener('click', () =>
    dropDown.classList.toggle('ul_dropDown-visible'),
    menuLinks.classList.remove('ul_dropDownLinks-visible')
  );
}
