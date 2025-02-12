from fastapi import FastAPI, Request
import requests

app = FastAPI()

# Данные для Supabase
SUPABASE_URL = "https://fmpbomqaxzaphpwfghis.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZtcGJvbXFheHphcGhwd2ZnaGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMzY2OTA5NSwiZXhwIjoyMDQ5MjQ1MDk1fQ.zuttQo4VFzxfgl8eJd4qC_Zt7ebpGtbP3YbVyRPtTpw"
TABLE_NAME = "productonline"

@app.get("/")
async def home():
    return {"message": "Webhook server is running!"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    
    # Проверяем, что это товар
    if "meta" in data and data["meta"].get("type") == "product":
        product_data = {
            "name": data.get("name"),
            "code": data.get("code"),
            "barcode": data["barcodes"][0]["ean"] if "barcodes" in data and data["barcodes"] else None,
            "price": data["salePrices"][0]["value"] / 100 if "salePrices" in data else None,
            "stock": data.get("quantity", None),
        }
        
        # Обрабатываем attributes
        if "attributes" in data and isinstance(data["attributes"], list):
            for attr in data["attributes"]:
                if attr["name"] == "Цвет":
                    product_data["color"] = attr["value"]
                if attr["name"] == "Размер":
                    product_data["size"] = attr["value"]
        
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
