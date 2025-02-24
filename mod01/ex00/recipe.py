
class Recipe:
    VALID_RECIPE_TYPE = {"starter", "lunch", "dessert"}

    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if (not isinstance(name, str)):
            print("Recipe name and ingredients must be valid strings")
            return
        elif (not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5):
            print("Recipe Cooking level must be an int between 1 and 5")
            return
        elif (not isinstance(cooking_time, int) or cooking_time < 0):
            print("Recipe Cooking level must be an int > 0")
            return
        elif (not isinstance(ingredients, str) and not isinstance(ingredients, list)):
            print("Recipe ingredients must be a list of valid string")
            return
        elif (description is not None and not isinstance(description, str)):
            print("Recipe description must be a valid string")
            return
        elif (not isinstance(recipe_type, str) or recipe_type not in self.VALID_RECIPE_TYPE):
            print("Recipe type must either be starter, lunch or dessert")
            return
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = "Recipe name is " + self.name + "\n"
        txt += "Cooking lvl is " + str(self.cooking_lvl) + "\n"
        txt += "Cooking time is " + str(self.cooking_time) + "\n"
        txt += "Ingredients are " + self.ingredients + "\n"
        txt += "Type of Recipe is " + self.recipe_type + "\n"
        return txt

#my_recipe = Recipe("Pizza", 5, 30, "Bread, Tomatoes", "", "lunch")

#print(my_recipe)