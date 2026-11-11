// Epic Building Group: the small amount of JavaScript the site uses. Every page is complete
// without it: this only adds the replay of the hero build, the pointer response on the hero,
// scroll reveals and the phone action bar's timing.
(function () {
  "use strict";
  var motion = window.matchMedia && matchMedia("(prefers-reduced-motion: no-preference)").matches;
  var fine = window.matchMedia && matchMedia("(hover: hover) and (pointer: fine)").matches;

  // Hero: replay the build, and lean the picture a little toward the pointer
  var hero = document.getElementById("hero");
  if (hero && motion) {
    var replay = document.getElementById("replay");
    if (replay) {
      replay.addEventListener("click", function () {
        hero.classList.add("is-reset");
        void hero.offsetWidth; // taking the animations off and on starts the build from the top
        hero.classList.remove("is-reset");
      });
    }
    if (fine) {
      var raf = 0;
      hero.addEventListener("pointermove", function (e) {
        if (raf) return;
        raf = requestAnimationFrame(function () {
          raf = 0;
          var r = hero.getBoundingClientRect();
          hero.style.setProperty("--px", (((e.clientX - r.left) / r.width) * 2 - 1).toFixed(3));
          hero.style.setProperty("--py", (((e.clientY - r.top) / r.height) * 2 - 1).toFixed(3));
        });
      });
      hero.addEventListener("pointerleave", function () {
        hero.style.setProperty("--px", 0);
        hero.style.setProperty("--py", 0);
      });
    }
  }

  // Reveal on scroll. Without IntersectionObserver everything simply shows.
  var reveals = document.querySelectorAll("[data-reveal]");
  if (motion && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add("is-in");
          io.unobserve(e.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 },
    );
    reveals.forEach(function (el) {
      io.observe(el);
    });
  } else {
    reveals.forEach(function (el) {
      el.classList.add("is-in");
    });
  }

  // Phone action bar: waits until the hero's own buttons have left the screen.
  var bar = document.getElementById("bar");
  var actions = document.getElementById("hero-actions");
  if (bar) {
    if (actions && "IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        bar.classList.toggle("is-on", !entries[0].isIntersecting);
      }).observe(actions);
    } else {
      bar.classList.add("is-on");
    }
  }

  // Close the phone menu when a link in it is used or Escape is pressed.
  var menu = document.querySelector(".menu");
  if (menu) {
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.open) {
        menu.open = false;
        menu.querySelector("summary").focus();
      }
    });
  }
})();
