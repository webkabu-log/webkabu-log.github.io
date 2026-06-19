document.addEventListener("DOMContentLoaded", () => {
  const atlas = document.querySelector(".atlas-container");
  if (!atlas) return;

  const paths = [...document.querySelectorAll(".atlas-timeline-path")];
  const containers = [...document.querySelectorAll(".atlas-timeline-container")];
  const reveals = [...document.querySelectorAll(".atlas-reveal, .atlas-stamp")];
  const chapters = [...document.querySelectorAll(".atlas-chapter[id^='chapter-']")];
  const navLinks = [...document.querySelectorAll(".atlas-nav-link")];
  const chapterNav = document.querySelector(".atlas-nav");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const supportsObserver = "IntersectionObserver" in window;
  let activeChapterId = "";
  let manualNavUntil = 0;
  let recenterTimer;

  const showEverything = () => {
    containers.forEach(container => container.classList.add("is-drawn"));
    reveals.forEach(element => element.classList.add("visible"));
  };

  const centerActiveLink = (link, force = false) => {
    if (!chapterNav || chapterNav.scrollWidth <= chapterNav.clientWidth + 1) return;

    if (!force && Date.now() < manualNavUntil) {
      clearTimeout(recenterTimer);
      recenterTimer = setTimeout(() => {
        if (link.getAttribute("href") === `#${activeChapterId}`) {
          centerActiveLink(link, true);
        }
      }, manualNavUntil - Date.now() + 30);
      return;
    }

    const left = link.offsetLeft - (chapterNav.clientWidth - link.offsetWidth) / 2;
    chapterNav.scrollTo({
      left: Math.max(0, left),
      behavior: reduceMotion.matches ? "auto" : "smooth"
    });
  };

  const setActiveChapter = id => {
    if (id === activeChapterId) return;
    activeChapterId = id;

    navLinks.forEach(link => {
      const active = link.getAttribute("href") === `#${id}`;
      link.classList.toggle("active", active);
      if (active) {
        link.setAttribute("aria-current", "location");
        centerActiveLink(link);
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  if (chapterNav) {
    const pauseAutoCenter = () => {
      manualNavUntil = Date.now() + 700;
    };

    chapterNav.addEventListener("pointerdown", pauseAutoCenter, { passive: true });
    chapterNav.addEventListener("touchstart", pauseAutoCenter, { passive: true });
    chapterNav.addEventListener("wheel", pauseAutoCenter, { passive: true });

    navLinks.forEach(link => {
      link.addEventListener("focus", () => centerActiveLink(link, true));
      link.addEventListener("click", () => centerActiveLink(link, true));
    });

    let resizeTimer;
    window.addEventListener("resize", () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        const activeLink = navLinks.find(link => link.getAttribute("href") === `#${activeChapterId}`);
        if (activeLink) centerActiveLink(activeLink, true);
      }, 120);
    }, { passive: true });
  }

  paths.forEach(path => {
    const length = path.getTotalLength();
    path.style.setProperty("--path-length", length);
  });

  if (!supportsObserver || reduceMotion.matches) {
    showEverything();
  } else {
    document.body.classList.add("js-active");

    const timelineObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-drawn");
        timelineObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12 });

    containers.forEach(container => timelineObserver.observe(container));

    const revealObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -6%" });

    reveals.forEach(element => revealObserver.observe(element));
  }

  if (supportsObserver && chapters.length && navLinks.length) {
    const visibleChapters = new Set();
    const updateActiveChapter = () => {
      const candidates = chapters.filter(chapter => visibleChapters.has(chapter));
      if (!candidates.length) return;
      const active = candidates.reduce((closest, chapter) => {
        const distance = Math.abs(chapter.getBoundingClientRect().top - 150);
        return !closest || distance < closest.distance ? { chapter, distance } : closest;
      }, null);
      setActiveChapter(active.chapter.id);
    };

    const chapterObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          visibleChapters.add(entry.target);
        } else {
          visibleChapters.delete(entry.target);
        }
      });
      updateActiveChapter();
    }, { rootMargin: "-12% 0px -68% 0px", threshold: 0 });

    chapters.forEach(chapter => chapterObserver.observe(chapter));
  } else if (chapters[0]) {
    setActiveChapter(chapters[0].id);
  }

  reduceMotion.addEventListener("change", event => {
    if (event.matches) {
      document.body.classList.remove("js-active");
      showEverything();
    }
  });
});
