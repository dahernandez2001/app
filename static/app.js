const BASE_URL = "http://127.0.0.1:5000";
let token = localStorage.getItem("token");

async function register() {
  const username = document.getElementById("register-username").value;
  const password = document.getElementById("register-password").value;
  const res = await fetch(`${BASE_URL}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });
  const data = await res.json();
  alert(data.msg);
}

async function login() {
  const username = document.getElementById("login-username").value;
  const password = document.getElementById("login-password").value;
  const res = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });
  const data = await res.json();
  if (data.access_token) {
    token = data.access_token;
    localStorage.setItem("token", token);
    document.getElementById("movie-section").classList.remove("hidden");
    alert("Login exitoso!");
    loadMovies();
  } else {
    alert("Error en login");
  }
}

async function loadMovies() {
  const res = await fetch(`${BASE_URL}/movies/`, {
    headers: { Authorization: `Bearer ${token}` }
  });
  const movies = await res.json();
  const list = document.getElementById("movie-list");
  list.innerHTML = "";
  movies.forEach(m => {
    const li = document.createElement("li");
    li.textContent = `${m.title} (${m.genre})`;
    list.appendChild(li);
  });
}

async function createMovie() {
  const title = document.getElementById("movie-title").value;
  const genre = document.getElementById("movie-genre").value;
  const res = await fetch(`${BASE_URL}/movies/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({ title, genre })
  });
  const data = await res.json();
  alert(data.msg || "Película agregada");
  loadMovies();
}
