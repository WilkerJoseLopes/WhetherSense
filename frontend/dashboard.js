(async function () {
  try {
    const weather = await getJson(`${API_BASE}/weather/current?localizacao=Lisboa`);
    const summary = await getJson(`${API_BASE}/analytics/summary?localizacao=Lisboa&dias=3`);

    document.getElementById("weatherBox").textContent = JSON.stringify(weather, null, 2);
    document.getElementById("summaryBox").textContent = JSON.stringify(summary, null, 2);
  } catch (error) {
    document.getElementById("weatherBox").textContent = "Erro ao carregar dados.";
    document.getElementById("summaryBox").textContent = error.message;
  }
})();
