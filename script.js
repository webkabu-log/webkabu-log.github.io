const incomeInput = document.getElementById("incomeInput");
const assetInput = document.getElementById("assetInput");
const memoOutput = document.getElementById("memoOutput");
const incomeTotal = document.getElementById("incomeTotal");

function formatYen(value) {
  return `${Number(value || 0).toLocaleString("ja-JP")}円`;
}

function updateMemo() {
  const income = Math.max(0, Number(incomeInput.value || 0));
  const asset = assetInput.value.trim() || "まだ決めない";
  const yen = formatYen(income);

  incomeTotal.textContent = yen;
  memoOutput.textContent = `今月は${yen}を投資候補にします。買うもの: ${asset}。`;
}

incomeInput.addEventListener("input", updateMemo);
assetInput.addEventListener("input", updateMemo);
updateMemo();
