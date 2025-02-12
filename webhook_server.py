from fastapi import FastAPI, Request
import requests

app = FastAPI()

# Данные для Supabase
SUPABASE_URL = "https://fmpbomqaxzaphpwfghis.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
TABLE_NAME = "productline"

@app.get("/")
async def home():
    return {"message": "Webhook server is running!"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    """Принимает данные от МойСклад и отправляет в Supabase"""
    data = await request.json()

    # Проверяем, что это товар
    if "meta" in data and "type" in data["meta"] and data["meta"]["type"] == "product":
        attributes = data.get("attributes", [])

        # Ищем цвет и размер в списке атрибутов
        color = next((attr["value"] for attr in attributes if attr.get("name") == "Цвет"), None)
        size = next((attr["value"] for attr in attributes if attr.get("name") == "Размер"), None)

        product_data = {
            "name": data.get("name"),
            "code": data.get("code"),
            "barcode": data.get("barcodes", [{}])[0].get("ean") if "barcodes" in data and data["barcodes"] else None,
            "price": data.get("salePrices", [{}])[0].get("value", 0) / 100 if "salePrices" in data else None,
            "stock": data.get("quantity") if "quantity" in data else None,
            "color": color,
            "size": size,
        }

        # Отправляем данные в Supabase
        headers = {
            "apikey": SUPABASE_API_KEY,
            "Content-Type": "application/json",
            "Authorization": f"Bearer {SUPABASE_API_KEY}"
        }

        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}",
            headers=headers,
            json=product_data
        )

        return {"status": response.status_code, "message": response.json()}

    return {"status": "error", "message": "Invalid webhook data"}
