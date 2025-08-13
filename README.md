# 🗺️ Local LLM + Google Maps Integration (Open WebUI)

This project integrates a **local LLM** via [Open WebUI](https://github.com/open-webui/open-webui) with the **Google Maps API** so you can ask in natural language for places to go/eat/etc., and get results as **embedded maps or links** directly in the chat.

---

## 📂 Project Structure
```
local-llm-maps/
│
├── google_maps_backend/
│   ├── main.py                  # FastAPI backend
│   ├── .env                     # Google Maps API key
│   ├── requirements.txt         # Backend Python dependencies
│
├── open-webui/                  # Cloned Open WebUI repo
│   ├── tools/
│   │   ├── __init__.py          # Tool package init
│   │   ├── google_maps_tool.py  # Our custom Google Maps integration
│   ├── docker-compose.yml
│   └── ...
│
└── README.md
```

---

## 1️⃣ Google Cloud API Key Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a **new project** (you get free $300 credit for 90 days).
3. Enable the following APIs:
   - **Places API**
   - **Directions API**
   - **Maps Embed API**
4. Create an **API key**.
5. Restrict the API key to **only your backend server’s IP** for security.

---

## 2️⃣ Install & Run Backend
```bash
cd google_maps_backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in `google_maps_backend/`:
```
GOOGLE_MAPS_API_KEY=YOUR_API_KEY
```

Run the backend:
```bash
uvicorn main:app --reload --port 9000
```

Backend runs at:
```
http://localhost:9000
```

---

## 3️⃣ Install & Run Open WebUI
```bash
cd ..
git clone https://github.com/open-webui/open-webui.git
cd open-webui
```

Place your custom tool:
```
open-webui/tools/google_maps_tool.py
open-webui/tools/__init__.py
```

Run with Docker:
```bash
docker compose up
```

Access the chat at:
```
http://localhost:8080
```

---

## 4️⃣ How to Use in Chat
Example prompts:
```
Find sushi restaurants near Senayan, Jakarta
Show me directions from Monas to Kota Tua
```

The LLM will:
1. Call the `google_maps_tool`.
2. Fetch results from your backend.
3. Display either an **embedded map** or a **Google Maps link**.
