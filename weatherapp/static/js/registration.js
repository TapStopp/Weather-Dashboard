document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("registrationForm");
  const backBtn = document.getElementById("backBtn");

  // Go back to Home
  backBtn.addEventListener("click", () => navigateTo("home"));

  // Validate and submit
  form.addEventListener("submit", e => {
    e.preventDefault();
    if (validateForm()) {
      alert("Registration successful!");
      navigateTo("profile");
    }
  });
});

function validateForm() {
  const fields = ["firstName", "lastName", "dob", "phone", "email"];
  for (let id of fields) {
    const input = document.getElementById(id);
    if (!input.value.trim()) {
      alert(`${id} cannot be empty`);
      input.focus();
      return false;
    }
  }
  return true;
}
