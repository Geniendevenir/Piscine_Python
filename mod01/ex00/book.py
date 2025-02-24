from recipe import Recipe
import datetime

class Book:
    VALID_BOOK_KEYS = {"starter", "lunch", "dessert"}

    def __init__(self, name, last_update, creation_date, recipe_list):
        if (not isinstance(name, str)):
            print("Name of the Book must be a Valid String")
            return
        elif(not isinstance(last_update, datetime.datetime) or not isinstance(creation_date, datetime.datetime)):
            print("Book creation date and modification time must be of format time: 0000/00/00")
            return
        if (not isinstance(recipe_list, dict) or set(recipe_list.keys()) != self.VALID_BOOK_KEYS):
            print("Recipe List must have three Keys: \'starter\', \'lunch\', \'dessert\'")
            return
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipe_list = recipe_list
    
    def __str__(self):
        txt = "Book name is " + self.name + "\n"
        txt += "Last Updated on " + str(self.last_update) + "\n"
        txt += "Added on " + str(self.creation_date) + "\n"
        return txt

    def get_recipe_name(self, name):
        if (not isinstance(name, str)):
            print("Invalid recipe name")
            return
        else:
            for catergory in self.recipe_list:
                if name in self.recipe_list[catergory]:
                    print(self.recipe_list["starter"][name])

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        for recipe_name in self.recipe_list[recipe_type].keys():
            print(recipe_name)

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        if (not isinstance(recipe, Recipe) or recipe.recipe_type not in self.recipe_list):
            print("The recipe argument needs to be a Recipe class instance")
            return
        self.recipe_list[recipe.recipe_type][recipe.name] = recipe
        self.last_update = datetime.datetime.now()
