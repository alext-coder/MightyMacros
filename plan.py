import services
import json


def process_day(intolerances):
    day_plan = []
    day_plan.append(process_recipes(intolerances,"breakfast")[0])
    day_plan.append(process_recipes(intolerances,"main course")[0])
    day_plan.append(process_recipes(intolerances,"main course")[1])
    return day_plan

def process_recipes(intolerances,meal_type):
    search_json =  services.process_restrictions(intolerances,meal_type)
    ids = [] 
    for result in search_json["results"]:
        ids.append(result["id"])
    ids_to_string = ",".join([str(id) for id in ids])
    recipes =  services.get_recipe_by_id(ids_to_string)
    result = []
    for recipe in recipes:
        cleaned_recipe = {}
        cleaned_recipe["title"] = recipe["title"]
        cleaned_recipe["ingredients"] = extract_ingredients(recipe)
        result.append(cleaned_recipe)
    return result


def extract_ingredients(recipe):
    cleaned_ingredients = []
    for ingredient in recipe["extendedIngredients"]:
        ingredient_data = {}
        ingredient_data["name"] = ingredient["name"]
        ingredient_data["amount"] = f"{ingredient["measures"]["us"]["amount"]} {ingredient["measures"]["us"]["unitShort"]}"
        cleaned_ingredients.append(ingredient_data)
    return cleaned_ingredients