/* Lu Lab — language toggle (zh-CN default) + mobile nav */
(function () {
  function setLang(lang) {
    document.documentElement.lang = lang;
    localStorage.setItem("lulab-lang", lang);
    document.querySelectorAll(".lang-toggle").forEach(function (btn) {
      btn.textContent = lang === "zh-CN" ? "EN" : "中文";
      btn.setAttribute("aria-label", lang === "zh-CN" ? "Switch to English" : "切换到中文");
    });
  }

  var current = document.documentElement.lang === "en" ? "en" : "zh-CN";

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".lang-toggle").forEach(function (btn) {
      btn.textContent = current === "zh-CN" ? "EN" : "中文";
      btn.addEventListener("click", function () {
        current = current === "zh-CN" ? "en" : "zh-CN";
        setLang(current);
      });
    });

    var burger = document.querySelector(".nav-hamburger");
    var nav = document.querySelector(".site-nav");
    if (burger && nav) {
      burger.addEventListener("click", function () {
        nav.classList.toggle("open");
      });
    }
  });
})();
