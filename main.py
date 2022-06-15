from string import ascii_lowercase
import requests


def get_cocktail(data):
    """
       Returns Cocktails with ingredients along with with measures.

       This function simply checks for the all given ingredients and then matches them with
       all the available cocktail ingredients to check if we can make a cocktail from given
       ingredients.

       Parameters
       ----------
       comma separated list of ingredients
       Example:
       Gin,Triple Sec,Lillet Blanc,Lemon Juice,Absinthe

       Returns
       -------
       list
           list of  the available cocktails from given ingredients.
       """

    # get all the cocktails list from given api
    all_cocktails = []
    for i in ascii_lowercase:
        response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={i}")
        if response.json()['drinks'] is None:
            continue
        all_cocktails = all_cocktails + response.json()['drinks']

    # parsing cocktail ingredients and Measures from cocktail list
    cocktail_ingredient = [
        {i["strDrink"]: [i["strIngredient1"], i["strIngredient2"],
                         i["strIngredient3"], i["strIngredient4"],
                         i["strIngredient5"], i["strIngredient6"],
                         i["strIngredient7"], i["strIngredient8"],
                         i["strIngredient9"], i["strIngredient10"],
                         i["strIngredient11"], i["strIngredient12"],
                         i["strIngredient13"], i["strIngredient14"],
                         i["strIngredient15"],
                         ],
         "Measures": [i["strMeasure1"], i["strMeasure2"],
                      i["strMeasure3"], i["strMeasure4"],
                      i["strMeasure5"], i["strMeasure6"],
                      i["strMeasure7"], i["strMeasure8"],
                      i["strMeasure9"], i["strMeasure10"],
                      i["strMeasure11"], i["strMeasure12"],
                      i["strMeasure13"], i["strMeasure14"],
                      i["strMeasure15"],
                      ]
         } for i in all_cocktails]
    # Removing None values from ingredients and measures
    cocktails = [{list(cocktail.keys())[0]: [i for i in list(cocktail.values())[0] if i],
                  list(cocktail.keys())[1]: [i for i in list(cocktail.values())[1] if i]
                  } for cocktail in cocktail_ingredient]

    # Result of the available cocktails from given ingredients
    res = []
    for i in cocktails:
        if set(list(i.values())[0]).issubset(data.split(',')):
            res.append(i)
            # printing list in terminal along with ingredients and measures
            print(f'{list(i.keys())[0]}: {list(i.values())[0]} , Measures: {list(i.values())[1]} \n')
    # Returning result to assert for in our TestCase
    return res


if __name__ == '__main__':
    while True:
        ingredients = input("Please Enter list of ingredients: ")
        get_cocktail(ingredients)
