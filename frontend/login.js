document.getElementById("loginBtn").addEventListener("click", async () => {
  const result = await postJson(`${API_BASE}/auth/google`, {
    google_id: "google-123",
    nome: "Utilizador Demo",
    email: "demo@weathersense.pt",
    foto_perfil: ""
  });

  localStorage.setItem("user", JSON.stringify(result.utilizador));
  window.location.href = "dashboard.html";
});
