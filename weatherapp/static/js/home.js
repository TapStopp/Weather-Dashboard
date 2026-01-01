document.addEventListener("DOMContentLoaded", () => {
  console.log("Home page loaded — Weather API integration coming soon!");

  // Example placeholder for future API
  const city = "Poughkeepsie";
  const temp = "72°F";
  const cond = "Sunny ☀️";

  document.getElementById("weatherCity").textContent = city;
  document.getElementById("weatherTemp").textContent = temp;
  document.getElementById("weatherCond").textContent = cond;
});
