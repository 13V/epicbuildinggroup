// Epic Building Group: the small amount of JavaScript the site uses. Every page is complete
// without it: this adds the replay of the hero build, the pointer response on the hero, scroll reveals,
// the full screen photographs, the stepped enquiry form and the phone action bar's timing.
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
    // depth: as the hero scrolls away the picture sinks and the words lift
    var sRaf = 0;
    var depth = function () {
      sRaf = 0;
      var h = hero.offsetHeight || 1;
      var v = Math.max(0, Math.min(1, window.scrollY / h));
      hero.style.setProperty("--sy", v.toFixed(3));
      hero.classList.toggle("is-away", v > 0.02);
    };
    window.addEventListener("scroll", function () {
      if (!sRaf) sRaf = requestAnimationFrame(depth);
    }, { passive: true });
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
  var reveals = document.querySelectorAll("[data-reveal], [data-draw], [data-stage]");
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

  // Rails (the build on a project page, the process): the red line fills as the page is read.
  var rails = [].slice.call(document.querySelectorAll("[data-rail]"));
  if (rails.length && motion) {
    var railRaf = 0;
    var fill = function () {
      railRaf = 0;
      var mid = window.innerHeight * 0.62;
      rails.forEach(function (r) {
        var b = r.getBoundingClientRect();
        var v = Math.max(0, Math.min(1, (mid - b.top) / Math.max(1, b.height)));
        r.style.setProperty("--rail", v.toFixed(3));
      });
    };
    var onScroll = function () {
      if (!railRaf) railRaf = requestAnimationFrame(fill);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    fill();
  }

  // Photographs open full screen. Each [data-zoom] link points at the image itself, so without
  // JavaScript it simply opens the photograph.
  var zooms = [].slice.call(document.querySelectorAll("a[data-zoom]"));
  if (zooms.length && typeof HTMLDialogElement !== "undefined") {
    var seen = {};
    var shots = zooms.filter(function (a) {
      if (seen[a.href]) return false;
      seen[a.href] = 1;
      return true;
    });
    var box = document.createElement("dialog");
    box.className = "lightbox";
    box.setAttribute("aria-label", "Photograph, full screen");
    box.innerHTML =
      '<div class="lb-top"><span class="label" data-lb-count></span><button class="lb-btn" type="button" data-lb-close aria-label="Close"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="square" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg></button></div>' +
      '<div class="lb-stage"><img alt=""><button class="lb-btn lb-prev" type="button" aria-label="Previous photograph"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="square" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button><button class="lb-btn lb-next" type="button" aria-label="Next photograph"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="square" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button></div>' +
      '<p class="lb-foot" data-lb-cap aria-live="polite"></p>';
    document.body.appendChild(box);
    var lbImg = box.querySelector("img");
    var at = 0;
    var opener = null;
    var show = function (i) {
      at = (i + shots.length) % shots.length;
      var a = shots[at];
      var inner = a.querySelector("img");
      lbImg.style.animation = "none";
      void lbImg.offsetWidth;
      lbImg.style.animation = "";
      lbImg.src = a.href;
      lbImg.alt = inner ? inner.alt : "";
      box.querySelector("[data-lb-cap]").textContent = inner ? inner.alt : "";
      box.querySelector("[data-lb-count]").textContent = at + 1 + " / " + shots.length;
      var many = shots.length > 1;
      box.querySelector(".lb-prev").hidden = !many;
      box.querySelector(".lb-next").hidden = !many;
    };
    zooms.forEach(function (a) {
      a.addEventListener("click", function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey) return;
        e.preventDefault();
        opener = a;
        var i = 0;
        shots.forEach(function (s, n) {
          if (s.href === a.href) i = n;
        });
        show(i);
        box.showModal();
      });
    });
    box.querySelector("[data-lb-close]").addEventListener("click", function () {
      box.close();
    });
    box.querySelector(".lb-prev").addEventListener("click", function () {
      show(at - 1);
    });
    box.querySelector(".lb-next").addEventListener("click", function () {
      show(at + 1);
    });
    box.addEventListener("click", function (e) {
      if (e.target === box || e.target.classList.contains("lb-stage")) box.close();
    });
    box.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") show(at - 1);
      if (e.key === "ArrowRight") show(at + 1);
    });
    box.addEventListener("close", function () {
      if (opener) opener.focus();
    });
    var x0 = null;
    box.addEventListener("touchstart", function (e) {
      x0 = e.touches[0].clientX;
    }, { passive: true });
    box.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      x0 = null;
      if (Math.abs(dx) > 50) show(at + (dx < 0 ? 1 : -1));
    });
  }

  // The enquiry form: three steps, checked as you go, with a success state.
  // HOOK: this is where the real endpoint goes. Post `data` as JSON and resolve only when the
  // enquiry has been received (reject otherwise, and the form tells the visitor to call).
  function sendEnquiry(data) {
    return new Promise(function (resolve) {
      window.console && console.log("Enquiry (demo, not sent):", data);
      setTimeout(resolve, 600);
    });
  }
  var form = document.getElementById("enquiry");
  if (form) {
    var steps = [].slice.call(form.querySelectorAll("[data-step]"));
    var dots = [].slice.call(form.querySelectorAll(".form-steps li"));
    var count = form.querySelector(".form-count");
    var back = form.querySelector("[data-back]");
    var next = form.querySelector("[data-next]");
    var qLabel = document.getElementById("q-label");
    var cur = 0;
    var setQuestion = function () {
      var c = form.querySelector('input[name="type"]:checked');
      if (c && qLabel) qLabel.textContent = c.getAttribute("data-q");
    };
    var go = function (i, focus) {
      cur = i;
      steps.forEach(function (st, n) {
        st.classList.toggle("is-current", n === i);
      });
      dots.forEach(function (d, n) {
        d.classList.toggle("is-on", n <= i);
      });
      back.hidden = i === 0;
      form.classList.toggle("is-last", i === steps.length - 1);
      count.textContent = "Step " + (i + 1) + " of " + steps.length;
      setQuestion();
      if (focus) {
        var f = steps[i].querySelector("input:not([type=radio]), select, textarea") || steps[i].querySelector("input");
        if (f) f.focus({ preventScroll: true });
        var top = form.getBoundingClientRect().top;
        if (top < 70) window.scrollBy({ top: top - 90, behavior: motion ? "smooth" : "auto" });
      }
    };
    var check = function (st) {
      var ok = true;
      var first = null;
      var fields = [].slice.call(st.querySelectorAll("input, select, textarea"));
      var radioDone = false;
      fields.forEach(function (f) {
        if (f.type === "radio") {
          if (radioDone) return;
          radioDone = true;
          var any = !!st.querySelector('input[type="radio"]:checked');
          var er = st.querySelector("[data-err]");
          if (er) er.hidden = any;
          if (!any) {
            ok = false;
            first = first || f;
          }
          return;
        }
        var valid = f.checkValidity();
        f.setAttribute("aria-invalid", valid ? "false" : "true");
        var msg = f.parentNode.querySelector(".err");
        if (msg) msg.hidden = valid;
        if (!valid) {
          ok = false;
          first = first || f;
        }
      });
      if (first) first.focus();
      return ok;
    };
    form.classList.add("is-stepped");
    // a choice made on the homepage arrives as ?type=
    var want = (location.search.match(/[?&]type=([a-z-]+)/) || [])[1];
    var pre = want && form.querySelector('input[name="type"][value="' + want + '"]');
    if (pre) pre.checked = true;
    go(pre ? 1 : 0, false);
    form.addEventListener("change", function (e) {
      if (e.target.name === "type") {
        setQuestion();
        var er = form.querySelector("[data-err]");
        if (er) er.hidden = true;
      }
    });
    form.addEventListener("input", function (e) {
      var f = e.target;
      if (f.getAttribute("aria-invalid") === "true" && f.checkValidity()) {
        f.setAttribute("aria-invalid", "false");
        var msg = f.parentNode.querySelector(".err");
        if (msg) msg.hidden = true;
      }
    });
    next.addEventListener("click", function () {
      if (check(steps[cur])) go(cur + 1, true);
    });
    back.addEventListener("click", function () {
      go(cur - 1, true);
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      for (var i = 0; i < steps.length; i++) {
        if (!check(steps[i])) {
          go(i, false);
          check(steps[i]);
          return;
        }
      }
      var data = {};
      [].slice.call(form.elements).forEach(function (f) {
        if (!f.name || (f.type === "radio" && !f.checked)) return;
        data[f.name] = f.value.trim();
      });
      data.question = qLabel ? qLabel.textContent : "";
      data.page = location.pathname;
      var send = form.querySelector("[data-send]");
      send.disabled = true;
      form.querySelector(".form-fail").hidden = true;
      sendEnquiry(data).then(
        function () {
          var done = form.querySelector(".form-done");
          done.querySelector("[data-done-name]").textContent = data.name ? ", " + data.name.split(" ")[0] : "";
          done.querySelector("[data-done-phone]").textContent = data.phone;
          form.classList.add("is-done");
          done.hidden = false;
          done.focus();
        },
        function () {
          send.disabled = false;
          form.querySelector(".form-fail").hidden = false;
        },
      );
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
