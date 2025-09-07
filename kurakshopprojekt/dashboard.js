document.addEventListener("DOMContentLoaded", function () {
  // Тема которуу
  const themeToggle = document.getElementById("themeToggle");
  themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("light");
  });

  // Chart.js - Line Chart
  const lineCtx = document.getElementById("lineChart").getContext("2d");
  new Chart(lineCtx, {
    type: "line",
    data: {
      labels: ["Янв", "Фев", "Мар", "Апр", "Май", "Июн"],
      datasets: [
        {
          label: "Сатуу динамикасы",
          data: [12, 19, 14, 20, 18, 22],
          borderColor: "#d4a373",
          backgroundColor: "rgba(212,163,115,0.2)",
          tension: 0.4,
          fill: true,
        },
      ],
    },
    options: { responsive: true },
  });

  // Chart.js - Bar Chart
  const barCtx = document.getElementById("barChart").getContext("2d");
  new Chart(barCtx, {
    type: "bar",
    data: {
      labels: ["Колдонуучулар", "Заказдар", "Товарлар"],
      datasets: [
        {
          label: "Статистика",
          data: [45, 28, 35],
          backgroundColor: ["#d4a373", "#f1c27d", "#8d6e63"],
        },
      ],
    },
    options: { responsive: true },
  });

  // Chart.js - Pie Chart
  const pieCtx = document.getElementById("pieChart").getContext("2d");
  new Chart(pieCtx, {
    type: "pie",
    data: {
      labels: ["Активдүү", "Токтотулган", "Жаңы"],
      datasets: [
        {
          data: [60, 25, 15],
          backgroundColor: ["#d4a373", "#8d6e63", "#f1c27d"],
        },
      ],
    },
    options: { responsive: true },
  });

  // DataTables
  $("#usersTable").DataTable();

  // Прогресс-баралар
  document.getElementById("progress1").style.width = "70%";
  document.getElementById("progress2").style.width = "50%";
});

document.addEventListener("DOMContentLoaded", function () {

  // -----------------------------
  // 1️⃣ Тема которуу (Dark / Light)
  // -----------------------------
  const themeToggle = document.getElementById("themeToggle");
  themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("light");
    // кнопканын текстин өзгөртүү
    if(document.body.classList.contains("light")){
      themeToggle.textContent = "🌙 Dark";
    } else {
      themeToggle.textContent = "☀️ Light";
    }
  });

  // -----------------------------
  // 2️⃣ Chart.js графиктер
  // -----------------------------

  // Line Chart – Сатуу динамикасы
  const lineCtx = document.getElementById("lineChart").getContext("2d");
  const lineChart = new Chart(lineCtx, {
    type: "line",
    data: {
      labels: ["Янв", "Фев", "Мар", "Апр", "Май", "Июн"],
      datasets: [{
        label: "Сатуу динамикасы",
        data: [12, 19, 14, 20, 18, 22],
        borderColor: "#d4a373",
        backgroundColor: "rgba(212,163,115,0.2)",
        tension: 0.4,
        fill: true
      }]
    },
    options: { responsive: true, plugins:{legend:{position:'top'}} }
  });

  // Bar Chart – Колдонуучу / Заказ / Товар статистикасы
  const barCtx = document.getElementById("barChart").getContext("2d");
  const barChart = new Chart(barCtx, {
    type: "bar",
    data: {
      labels: ["Колдонуучулар", "Заказдар", "Товарлар"],
      datasets: [{
        label: "Статистика",
        data: [45, 28, 35],
        backgroundColor: ["#d4a373", "#f1c27d", "#8d6e63"]
      }]
    },
    options: { responsive: true, plugins:{legend:{position:'top'}} }
  });

  // Pie Chart – Колдонуучунун статусу
  const pieCtx = document.getElementById("pieChart").getContext("2d");
  const pieChart = new Chart(pieCtx, {
    type: "pie",
    data: {
      labels: ["Активдүү", "Токтотулган", "Жаңы"],
      datasets: [{
        data: [60, 25, 15],
        backgroundColor: ["#d4a373", "#8d6e63", "#f1c27d"]
      }]
    },
    options: { responsive: true, plugins:{legend:{position:'bottom'}} }
  });

  // -----------------------------
  // 3️⃣ DataTables таблица
  // -----------------------------
  $("#usersTable").DataTable({
    paging: true,
    searching: true,
    ordering: true,
    info: true,
    pageLength: 5
  });

  // -----------------------------
  // 4️⃣ Прогресс-бары
  // -----------------------------
  const progressBars = [
    {id: "progress1", value: 70},
    {id: "progress2", value: 50}
  ];

  progressBars.forEach(bar => {
    const el = document.getElementById(bar.id);
    let width = 0;
    const interval = setInterval(() => {
      if(width >= bar.value) clearInterval(interval);
      else {
        width++;
        el.style.width = width + "%";
      }
    }, 10);
  });

  // -----------------------------
  // 5️⃣ Дополнительные интерактивные функции
  // -----------------------------

  // Меню ачуу/жабуу (эгер админкада dropdown меню болсо)
  const menuItems = document.querySelectorAll('.menu-item');
  menuItems.forEach(item => {
    item.addEventListener('click', () => {
      const dropdown = item.nextElementSibling;
      if(dropdown && dropdown.classList.contains('dropdown')){
        dropdown.style.display = dropdown.style.display==='flex'?'none':'flex';
      }
    });
  });

  console.log("Dashboard JS иштеп жатат ✅");
});
