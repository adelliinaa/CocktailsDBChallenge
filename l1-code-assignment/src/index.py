import requests
import json
from collections import defaultdict

def cocktails():

    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?f=g"
    data = requests.get(f)
    drinks = json.loads(data.text)
    cocktail_index = 0
    cocktail_name = []
    cocktails_with_min_4_ingredients = []
    cocktail_id_name_ingredients = []
    cocktail_ingredient_quantities = []
    ingredients = defaultdict(list)
    alcoholic = []
    non_alcoholic = []
    
    for i in (drinks["drinks"]):

        cocktail_info_dict = dict()
        cocktail_info_dict_quantities = dict()
        ingredient_quantities = []
        cocktail_name.append(i["strDrink"])
        # parse the cocktail information if it has more than 4 ingredients
        if i["strIngredient5"] != None:
            cocktails_with_min_4_ingredients.append((i["strDrink"]))
        cocktail_index += 1
        for ingredient_no in range(1, 15):
            if i[f"strIngredient{ingredient_no}"] != None:
                ingredients[i["strDrink"]].append(i[f"strIngredient{ingredient_no}"])
                quantities = dict()
                quantities["name"] = i[f"strIngredient{ingredient_no}"]
                quantities["quantity"] = i[f"strMeasure{ingredient_no}"]
                ingredient_quantities.append(quantities)
            else:
                break

        cocktail_info_dict["name"] = i["strDrink"]
        cocktail_info_dict["id"] = i["idDrink"]
        cocktail_info_dict["ingredients"] = ingredients[i["strDrink"]]
        cocktail_id_name_ingredients.append(cocktail_info_dict)

        cocktail_info_dict_quantities["name"] = i["strDrink"]
        cocktail_info_dict_quantities["id"] = i["idDrink"]
        cocktail_info_dict_quantities["ingredients"] = ingredient_quantities
        cocktail_ingredient_quantities.append(cocktail_info_dict_quantities)
        if i["strAlcoholic"] == "Alcoholic":
            alcoholic.append(cocktail_info_dict_quantities)
        else:
            non_alcoholic.append(cocktail_info_dict_quantities)
    print("Cocktails beiginning with G:")
    print(f"Total: {cocktail_index}")
    print(f"Names: {cocktail_name}", "\n")
    print("Cocktails with more than 4 ingredients:")
    print(cocktails_with_min_4_ingredients, "\n")
    print("Cocktails with just id/name/ingredients:")
    print(cocktail_id_name_ingredients, "\n")
    print("Cocktails with ingredient quantities:")
    print(cocktail_ingredient_quantities, "\n")
    print("Alcoholic / Non-alcoholic cocktails:")
    print("Alcoholic:")
    print(alcoholic)
    print("Non-Alcoholic:")
    print(non_alcoholic)

cocktails()

