function toggleDropdown(dropdownId) {
    // Закрыть все открытые dropdown перед открытием текущего
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
      if (dropdowns[i].id !== dropdownId) {
        dropdowns[i].classList.remove("show");
      }
    }
  
    // Открыть или закрыть выбранное меню
    document.getElementById(dropdownId).classList.toggle("show");
  }
  
  // Закрытие выпадающих меню при клике за пределами
  window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  };
