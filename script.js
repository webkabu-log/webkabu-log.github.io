const yenFormatter = new Intl.NumberFormat("ja-JP");

function yen(value) {
  return `${yenFormatter.format(Number(value || 0))}円`;
}

const revealItems = document.querySelectorAll(".reveal");
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.16 }
);

revealItems.forEach((item, index) => {
  item.style.transitionDelay = `${Math.min(index * 45, 260)}ms`;
  revealObserver.observe(item);
});

document.querySelectorAll(".count-up").forEach((item) => {
  const target = Number(item.dataset.target || 0);
  const startedAt = performance.now();
  const duration = 900;

  function tick(now) {
    const progress = Math.min((now - startedAt) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    item.textContent = yen(Math.round(target * eased));

    if (progress < 1) {
      requestAnimationFrame(tick);
    }
  }

  requestAnimationFrame(tick);
});

document.querySelectorAll(".nav").forEach((nav) => {
  const toggle = nav.querySelector(".nav-toggle");
  const links = nav.querySelectorAll(".nav-links a");
  const currentFile = window.location.pathname.split("/").pop() || "index.html";

  if (!toggle) {
    return;
  }

  links.forEach((link) => {
    const linkUrl = new URL(link.getAttribute("href"), window.location.href);
    const linkFile = linkUrl.pathname.split("/").pop() || "index.html";

    if (linkFile === currentFile && !link.hash) {
      link.setAttribute("aria-current", "page");
    }
  });

  function closeMenu() {
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "メニューを開く");
    nav.classList.remove("nav-open");
  }

  toggle.addEventListener("click", () => {
    const isOpen = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!isOpen));
    toggle.setAttribute("aria-label", isOpen ? "メニューを開く" : "メニューを閉じる");
    nav.classList.toggle("nav-open", !isOpen);
  });

  links.forEach((link) => {
    link.addEventListener("click", () => {
      closeMenu();
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
    }
  });
});
