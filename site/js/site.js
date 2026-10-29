/* Portfolio: project filter and footer year. Without JS every project shows. */
(function () {
  "use strict";
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  var chips = document.querySelectorAll(".chip");
  var cards = document.querySelectorAll(".card");
  var status = document.getElementById("filter-status");

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      var f = chip.dataset.filter, shown = 0;
      chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
      cards.forEach(function (card) {
        var on = f === "all" || card.dataset.group === f;
        card.hidden = !on;
        if (on) shown++;
      });
      document.querySelectorAll(".grid").forEach(function (g) {
        g.hidden = !g.querySelector(".card:not([hidden])");
      });
      status.textContent = "Showing " + shown + " project" + (shown === 1 ? "" : "s") + ".";
    });
  });
})();
