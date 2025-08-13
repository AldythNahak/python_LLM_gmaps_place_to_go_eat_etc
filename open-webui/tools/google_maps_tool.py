import requests
from typing import Dict

def google_maps_tool(params: Dict) -> str:
    """
    Tool for searching places or directions using the backend API.
    params:
      action: "places" or "directions"
      query: search text (for places)
      origin: origin location string (for directions)
      destination: destination location string (for directions)
    """
    backend_url = "http://localhost:9000"
    
    if params.get("action") == "places":
        r = requests.get(f"{backend_url}/places", params={
            "query": params["query"],
            "location": params.get("location", "0,0"),
            "radius": params.get("radius", 5000)
        })
        data = r.json()
        results_html = "<b>Places found:</b><br>"
        for place in data.get("results", []):
            name = place.get("name", "Unknown")
            address = place.get("formatted_address", "No address")
            lat = place["geometry"]["location"]["lat"]
            lng = place["geometry"]["location"]["lng"]
            link = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
            results_html += f"• <a href='{link}' target='_blank'>{name}</a> — {address}<br>"
        return results_html

    elif params.get("action") == "directions":
        r = requests.get(f"{backend_url}/directions", params={
            "origin": params["origin"],
            "destination": params["destination"],
            "mode": params.get("mode", "driving")
        })
        link = f"https://www.google.com/maps/dir/?api=1&origin={params['origin']}&destination={params['destination']}&travelmode={params.get('mode', 'driving')}"
        return f"<a href='{link}' target='_blank'>Open Directions in Google Maps</a>"

    return "Invalid parameters."
