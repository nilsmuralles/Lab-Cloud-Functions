import os
import requests
import functions_framework

@functions_framework.http
def maps_query(request):
    place = request.args.get("place", "")

    if not place:
        return {"error": "Parámetro 'place' requerido. Ejemplo: ?place=Mercado+Central+Guatemala"}, 400

    api_key = os.environ.get("MAPS_KEY")
    if not api_key:
        return {"error": "API Key no configurada en el servidor"}, 500

    resp = requests.get(
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json",
        params={
            "input": place,
            "inputtype": "textquery",
            "fields": "place_id,name,geometry,formatted_address,rating,opening_hours",
            "key": api_key,
        }
    )

    return resp.json()
