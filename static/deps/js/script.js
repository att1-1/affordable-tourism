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
  if (!event.target.closest('.dropdown')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      for (var i = 0; i < dropdowns.length; i++) {
          dropdowns[i].classList.remove("show");
      }
  }
};


  document.querySelectorAll(".btn-submit").forEach((button) => {
    button.addEventListener("click", function (event) {
      // Остановить стандартное поведение формы
      event.preventDefault();
  
      // Получить форму, к которой принадлежит кнопка
      const form = button.closest("form");
  
      // Создать объект URLSearchParams для всех параметров формы
      const params = new URLSearchParams(new FormData(form));
  
      // Обновить строку запроса
      const newUrl = `${window.location.pathname}?${params.toString()}`;
      window.history.replaceState(null, "", newUrl);
  
      // Перезагрузить страницу с новыми параметрами
      window.location.reload();
    });
  });
  
