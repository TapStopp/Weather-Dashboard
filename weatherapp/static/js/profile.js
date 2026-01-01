document.addEventListener("DOMContentLoaded", () => {
  const backBtn = document.getElementById("backBtn");
  const saveBtn = document.getElementById("saveBtn");

  backBtn.addEventListener("click", () => navigateTo("home"));
  saveBtn.addEventListener("click", saveProfile);
});

function saveProfile() {
  const first = document.getElementById("pFirst").value;
  const last = document.getElementById("pLast").value;
  const phone = document.getElementById("pPhone").value;
  const email = document.getElementById("pEmail").value;

  alert(`Saved:\n${first} ${last}\n${phone}\n${email}`);
}
