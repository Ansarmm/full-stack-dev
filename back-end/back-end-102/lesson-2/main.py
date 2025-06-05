from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Эндпоинт /health позволяет убедиться, что сервер запущен и отвечает на запросы. А также быстро обнаружить проблемы.