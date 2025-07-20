const form = document.getElementById("feedbackForm");
const responseBox = document.getElementById("response");
const feedbackList = document.getElementById("feedbackList");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("message").value;

  const res = await fetch("http://127.0.0.1:8000/feedback", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, message })
  });

  const data = await res.json();
  responseBox.textContent = data.message;
  form.reset();
  loadFeedbacks();
});

async function loadFeedbacks() {
  const res = await fetch("http://127.0.0.1:8000/feedback");
  const data = await res.json();
  feedbackList.innerHTML = "";
  data.feedbacks.forEach(fb => {
    const div = document.createElement("div");
    div.className = "feedback-item";
    div.innerHTML = `<strong>${fb.name}</strong> (${fb.email})<br>${fb.message}<br><small>${fb.timestamp}</small>`;
    feedbackList.appendChild(div);
  });
}

window.onload = loadFeedbacks;
