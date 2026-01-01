document.addEventListener("DOMContentLoaded", () => {
  const message = document.getElementById("continueMessage");

  // Smooth fade animation
  let fade = true;
  setInterval(() => {
    message.style.opacity = fade ? 0 : 1;
    fade = !fade;
  }, 1200);

  // Listen for keydown anywhere
  window.addEventListener("keydown", e => {
    if (e.code === "Space" || e.key === " ") {
      e.preventDefault(); // prevent scroll
      navigateTo("home");
    }
  });

  // Allow click to continue
  message.addEventListener("click", () => navigateTo("home"));
});
