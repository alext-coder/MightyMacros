import os
import requests

api_key = os.environ.get("API_KEY")
api_url = "https://api.spoonacular.com/recipes/complexSearch"

params = {
    "apiKey" : api_key,
    "query" : "pasta",
    "number" : 5,

}

if __name__ == "__main__":
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Recipes found:")
        for recipe in data.get("results", []):
            print(f"- {recipe['title']}")
    else:      
        print(f"Error: {response.status_code}, {response.text}")