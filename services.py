import os
import requests

api_key = os.environ.get("API_KEY")




def process_restrictions(intolerances):
    
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey" : api_key,
        "number" : 5,
    }   
    if intolerances:
        params["intolerances"] = intolerances
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_recipe_by_id(ids):
    url = "https://api.spoonacular.com/recipes/informationBulk"
    params = {
        "apiKey" : api_key,
        "ids" : ids,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
