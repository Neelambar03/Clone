// Tab switching
const tabs = document.querySelectorAll(".tab");
const contents = document.querySelectorAll(".tab-content");

tabs.forEach(tab => {
  tab.addEventListener("click", () => {
    tabs.forEach(t => t.classList.remove("active"));
    tab.classList.add("active");

    contents.forEach(c => c.classList.add("hidden"));
    document.getElementById(tab.dataset.tab).classList.remove("hidden");
  });
});

// Review submission
const form = document.getElementById("review-form");
const reviewList = document.getElementById("review-list");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.getElementById("reviewer").value;
  const text = document.getElementById("review-text").value;

  const review = document.createElement("div");
  review.innerHTML = `<p><strong>${name}</strong>: ${text}</p>`;
  reviewList.appendChild(review);

  form.reset();
});

// Compare + Notify buttons
document.getElementById("compare-btn").onclick = () => alert("Added to Compare List!");
document.getElementById("notify-btn").onclick = () => alert("You will be notified when available!");

// Dark mode toggle
const themeBtn = document.getElementById("theme-toggle");
themeBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  themeBtn.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";
});
