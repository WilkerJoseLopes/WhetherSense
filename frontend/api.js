const API_BASE = "https://weathersense-backend.onrender.com/api/v1";

async function getJson(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error("Erro na API");
  return response.json();
}

async function postJson(url, body) {
  const response = await fetch(url, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(body)
  });

  if (!response.ok) throw new Error("Erro ao enviar");
  return response.json();
}
