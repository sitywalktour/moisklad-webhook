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
    """Принимает данные от МойСклад и отправляет в Supabase"""
    data = await request.json()

    # Проверяем, что это товар
    if "meta" in data and "type" in data["meta"] and data["meta"]["type"] == "product":
        product_data = {
            "name": data.get("name"),
            "code": data.get("code"),
            "barcode": data.get("barcodes", [{}])[0].get("ean") if "barcodes" in data else None,
            "price": data.get("salePrices", [{}])[0].get("value") / 100 if "salePrices" in data else None,
            "stock": data.get("quantity") if "quantity" in data else None,
            "color": data.get("attributes", {}).get("Цвет", None),
            "size": data.get("attributes", {}).get("Размер", None),
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

    return {"status": "error", "message": "Invalid webhook data"}from fastapi import FastAPI, Request
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
    """Принимает данные от МойСклад и отправляет в Supabase"""
    data = await request.json()

    # Проверяем, что это товар
    if "meta" in data and "type" in data["meta"] and data["meta"]["type"] == "product":
        product_data = {
            "name": data.get("name"),
            "code": data.get("code"),
            "barcode": data.get("barcodes", [{}])[0].get("ean") if "barcodes" in data else None,
            "price": data.get("salePrices", [{}])[0].get("value") / 100 if "salePrices" in data else None,
            "stock": data.get("quantity") if "quantity" in data else None,
            "color": data.get("attributes", {}).get("Цвет", None),
            "size": data.get("attributes", {}).get("Размер", None),
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

    return {"status": "error", "message": "Invalid webhook data"}from fastapi import FastAPI, Request
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
    """Принимает данные от МойСклад и отправляет в Supabase"""
    data = await request.json()

    # Проверяем, что это товар
    if "meta" in data and "type" in data["meta"] and data["meta"]["type"] == "product":
        product_data = {
            "name": data.get("name"),
            "code": data.get("code"),
            "barcode": data.get("barcodes", [{}])[0].get("ean") if "barcodes" in data else None,
            "price": data.get("salePrices", [{}])[0].get("value") / 100 if "salePrices" in data else None,
            "stock": data.get("quantity") if "quantity" in data else None,
            "color": data.get("attributes", {}).get("Цвет", None),
            "size": data.get("attributes", {}).get("Размер", None),
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

    return {"status": "error", "message": "Invalid webhook data"}from fastapi import FastAPI, Request
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
    """Принимает данные от МойСклад и отправляет в Supabase"""
    data = await request.json()

    # Проверяем, что это товар
    if "meta" in data and "type" in data["meta"] and data["meta"]["type"] == "product":
        product_data = {
            "name": data.get("name"),
            "code": data.get("code"),
            "barcode": data.get("barcodes", [{}])[0].get("ean") if "barcodes" in data else None,
            "price": data.get("salePrices", [{}])[0].get("value", 0) / 100 if "salePrices" in data else None,
            "stock": data.get("quantity") if "quantity" in data else None,
            "color": data.get("attributes", {}).get("Цвет", None),
            "size": data.get("attributes", {}).get("Размер", None)
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
from fastapi import FastAPI, Request
import requests

app = FastAPI()

# Маршрут для проверки работы сервера
@app.get("/")
async def home():
    return {"message": "Webhook server is running!"}

# Данные для Supabase
SUPABASE_URL = "https://fmpboagxazpwhgfwghis.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
TABLE_NAME = "productline"

@app.post("/webhook")
async def receive_webhook(request: Request):
    """Принимает данные от МойСклад и отправляет в Supabase"""
    data = await request.json()

    # Проверяем, что это товар
    if "meta" in data and "type" in data["meta"] and data["meta"]["type"] == "product":
        product_data = {
            "name": data.get("name"),
            "code": data.get("code"),
            "barcode": data.get("barcodes")[0]["ean"] if "barcodes" in data and data["barcodes"] else None,
            "price": data.get("salePrices", [{}])[0].get("value", 0) / 100 if "salePrices" in data else None,
            "stock": data.get("quantity") if "quantity" in data else None,
            "color": data.get("attributes", {}).get("Цвет", None),
            "size": data.get("attributes", {}).get("Размер", None),
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

    return {"status": "error", "message": "Invalid webhook data"}@app.get("/")
def home():
    return {"message": "Webhook server is running!"}from fastapi import FastAPI, Request
import requests

app = FastAPI()

# Данные для Supabase
SUPABASE_URL = "https://fmpbomqaxzaphpwfghis.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
TABLE_NAME = "productonline"

@app.post("/webhook")
async def receive_webhook(request: Request):
    """Принимает данные от МойСклад и отправляет в Supabase"""
    data = await request.json()

    # Проверяем, что это товар
    if "meta" in data and "type" in data["meta"] and data["meta"]["type"] == "product":
        product_data = {
            "name": data.get("name"),
            "code": data.get("code"),
            "barcode": data.get("barcodes")[0]["ean"] if "barcodes" in data and data["barcodes"] else None,
            "price": data.get("salePrices")[0]["value"] / 100 if "salePrices" in data else None,
            "stock": data.get("quantity") if "quantity" in data else None,
            "color": data.get("attributes", {}).get("Цвет", None),
            "size": data.get("attributes", {}).get("Размер", None)
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
