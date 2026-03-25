from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx

app = FastAPI(title="WeatherSense API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

@app.get("/")
def root():
    return {"message": "WeatherSense backend online"}

@app.get("/api/v1/health")
def health():
    return {"status": "ok"}

@app.post("/api/v1/auth/google")
def auth_google(payload: dict):
    return {
        "mensagem": "Login simulado com sucesso",
        "utilizador": payload
    }

@app.get("/api/v1/weather/current")
async def current(localizacao: str = Query(...)):
    if not OPENWEATHER_API_KEY:
        return {
            "localizacao": localizacao,
            "temperatura": 19,
            "humidade": 64,
            "vento": 12,
            "condicao": "Parcialmente nublado"
        }

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": localizacao,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "pt"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()

    return {
        "localizacao": data["name"],
        "temperatura": data["main"]["temp"],
        "humidade": data["main"]["humidity"],
        "vento": data["wind"]["speed"],
        "condicao": data["weather"][0]["description"]
    }

@app.get("/api/v1/weather/forecast")
def forecast(localizacao: str):
    return {
        "localizacao": localizacao,
        "previsoes": [
            {"dia": "Seg", "temp": 18, "condicao": "Nublado"},
            {"dia": "Ter", "temp": 20, "condicao": "Sol"},
            {"dia": "Qua", "temp": 17, "condicao": "Chuva"}
        ]
    }

@app.get("/api/v1/history")
def history(localizacao: str, inicio: str, fim: str):
    return {
        "localizacao": localizacao,
        "inicio": inicio,
        "fim": fim,
        "dados": [
            {"data": "2025-05-01", "temperatura": 18.4},
            {"data": "2025-05-02", "temperatura": 17.2}
        ]
    }

@app.get("/api/v1/analytics/summary")
def summary(localizacao: str, dias: int = 3):
    return {
        "localizacao": localizacao,
        "resumo": f"Nos próximos {dias} dias prevê-se tempo estável e baixa probabilidade de chuva."
    }

@app.get("/api/v1/analytics/report")
def report(localizacao: str, dias: int = 7):
    return {
        "localizacao": localizacao,
        "dias": dias,
        "precisao": 89,
        "conclusao": "Boa precisão no período analisado."
    }

@app.post("/api/v1/complaints")
def create_complaint(payload: dict):
    return {
        "estado": "Pendente",
        "mensagem": "Reclamação submetida com sucesso.",
        "dados": payload
    }

@app.get("/api/v1/notifications/my")
def notifications():
    return [
        {
            "id": "1",
            "titulo": "Alerta meteorológico",
            "mensagem": "Possibilidade de chuva nas próximas horas.",
            "lida": False
        }
    ]
