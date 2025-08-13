from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_MAPS_SERVER_KEY = os.getenv("GOOGLE_MAPS_SERVER_KEY")

if not GOOGLE_MAPS_SERVER_KEY:
    raise RuntimeError("Missing GOOGLE_MAPS_SERVER_KEY in .env")

app = FastAPI()

# Allow Open WebUI frontend to call this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/places")
def search_places(query: str = Query(...), location: str = Query("0,0"), radius: int = Query(5000)):
    """Search for places using Google Places API"""
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "location": location,
        "radius": radius,
        "key": GOOGLE_MAPS_SERVER_KEY
    }
    r = requests.get(url, params=params)
    if r.status_code != 200:
        raise HTTPException(status_code=500, detail="Google Maps API error")
    return r.json()

@app.get("/directions")
def get_directions(origin: str, destination: str, mode: str = "driving"):
    """Get directions using Google Directions API"""
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": mode,
        "key": GOOGLE_MAPS_SERVER_KEY
    }
    r = requests.get(url, params=params)
    if r.status_code != 200:
        raise HTTPException(status_code=500, detail="Google Maps API error")
    return r.json()
