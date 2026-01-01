function navigateTo(page) {
  switch (page) {
    case "home":
      window.location.href = "home.html";
      break;
    case "registration":
      window.location.href = "registration.html";
      break;
    case "profile":
      window.location.href = "profile.html";
      break;
    case "login":
      alert("Login functionality coming soon!");
      break;
    default:
      window.location.href = "index.html";
  }
}
