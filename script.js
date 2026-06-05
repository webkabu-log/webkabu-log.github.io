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

const incomeRange = document.getElementById("incomeRange");
const rangeValue = document.getElementById("rangeValue");
const rangeText = document.getElementById("rangeText");

function updateRange() {
  const amount = Number(incomeRange.value || 0);
  rangeValue.textContent = yen(amount);

  if (amount === 0) {
    rangeText.textContent = "まだ投資はしません。まずはWeb収益の発生を待ちます。";
    return;
  }

  if (amount < 1000) {
    rangeText.textContent = "小さな一歩です。買う前に、候補を調べる段階です。";
    return;
  }

  if (amount < 5000) {
    rangeText.textContent = "少額投資を検討できる金額です。理由を決めてから動きます。";
    return;
  }

  rangeText.textContent = "選択肢が増えます。ただし生活費とは混ぜず、収益の範囲だけで進めます。";
}

incomeRange.addEventListener("input", updateRange);
updateRange();
