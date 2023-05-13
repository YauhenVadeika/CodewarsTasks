"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def cakes(recipe, available):

    return min([
        available[key] // recipe[key] if key in available else 0
        for key in recipe
    ])


print(
    cakes({
        "flour": 500,
        "sugar": 200,
        "eggs": 1
    }, {
        "flour": 1200,
        "sugar": 1200,
        "eggs": 5,
        "milk": 200
    }))  # --> 2
print(
    cakes({
        'cream': 200,
        'flour': 300,
        'sugar': 150,
        'milk': 100,
        'oil': 100
    }, {
        'sugar': 1700,
        'flour': 20000,
        'milk': 20000,
        'oil': 30000,
        'cream': 5000
    }))  # --> 25 should equal 11


# codewars task best solution
def cakes(recipe, available):
    return min(available.get(k, 0) / recipe[k] for k in recipe)


# codewars task best solution
def cakes(recipe, available):
    try:
        return min([available[a] / recipe[a] for a in recipe])
    except:
        return 0


# codewars task best solution
def cakes(recipe, available):
    ''' Take each ingredient from the recipe, see if it is in the available ones
        and calculate how many full cakes you can make with it.
        If an ingredient is missing, we can't bake a cake. Otherwise we have to
        find the lowest possible amount of cakes.'''
    return min(
        [available[i] // recipe[i] if i in available else 0 for i in recipe])


# codewars task best solution
def cakes(recipe, available):
    list = []
    for ingredient in recipe:
        if ingredient in available:
            list.append(available[ingredient] / recipe[ingredient])
        else:
            return 0
    return min(list)


# codewars task best solution
def cakes(recipe, available):
    return min(available.get(k, 0) // v for k, v in recipe.iteritems())


# codewars task best solution
def cakes(recipe, ingredients):
    return min(ingredients.get(k, 0) / v for k, v in recipe.iteritems())


# codewars task best solution
def cakes(recipe, available):
    amount_per_ingredient = []
    for ingredient in recipe:
        if ingredient not in available or available[ingredient] < recipe[
                ingredient]:
            return 0
        else:
            amount_per_ingredient.append(available[ingredient] /
                                         recipe[ingredient])
    return min(amount_per_ingredient)


# codewars task best solution
def cakes(recipe, available):
    return min((available.get(k, 0) // v for k, v in recipe.items()))