from app import app, db
from models.Cocktail import Cocktail
import requests


with app.app_context():
    db.drop_all()
    db.create_all()

    # TEST SEEDS:
    # all_cocktails = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Egg').json()

    all_cocktails = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Alcoholic').json()

    for each_cocktail in all_cocktails['drinks']:
        print(each_cocktail['strDrink'] + ' ' + each_cocktail['idDrink'])

        one_cocktail = requests.get(
            'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}'.format(each_cocktail['idDrink'])
        ).json()
        cocktail_name = each_cocktail['strDrink'].replace(" ", "_")

        cocktail_name = Cocktail({
            'name': one_cocktail['drinks'][0]['strDrink'],
            'method': one_cocktail['drinks'][0]['strInstructions'],
            'image': one_cocktail['drinks'][0]['strDrinkThumb'],
        })

        i = 1
        while i < 15:

            if (one_cocktail['drinks'][0]['strIngredient{}'.format(i)] != '' and one_cocktail['drinks'][0]['strIngredient{}'.format(i)] is not None):

                ingr_type = one_cocktail['drinks'][0]['strIngredient{}'.format(i)]
                ingr_amount = one_cocktail['drinks'][0]['strMeasure{}'.format(i)]
                print(ingr_type)
                cocktail_name.add_ingredients([{"amount": ingr_amount, "name": ingr_type}])
            else:
                print('this cocktail has no {}th ingredient'.format(i))

            i += 1

        cocktail_name.save()
