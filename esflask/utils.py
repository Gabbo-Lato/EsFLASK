import requests

def richiesta():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    dati = response.json()
    return dati

def get_random_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("fact", "Nessun fatto disponibile")
    else:
        return "Impossibile recuperare"