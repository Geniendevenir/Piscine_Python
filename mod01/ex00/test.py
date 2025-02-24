from recipe import Recipe
from book import Book
import datetime

my_book = Book(
    "Gamgam_Recipe", 
    datetime.datetime.now(), 
    datetime.datetime.now(), 
    {
        "starter": {
            "Salad": Recipe ("Salad", 1 , 15, "Letuce, Garlic", "", "starter")
                    },
        "lunch": {
             "Pasta": Recipe("Pasta", 2, 30, "Pasta, Tomatoes", "", "lunch")
        },
        "dessert": {
            "Icecream": Recipe("Icecream", 4, 60, "Cream, Strawberry", "", "dessert")
        }
    })

print(my_book)
print(my_book.last_update)
my_book.get_recipe_name("Salad")
my_book.add_recipe(Recipe("Couilles_de_coq", 5, 120, "Couilles de coq", "", "starter"))
my_book.get_recipes_by_types("starter")
print(my_book.last_update)
my_book.get_recipe_name("Couilles_de_coq")

Nested_Dict_class = {
        "starter": {
            "Salad": Recipe ("Salad", 1 , 15, "Letuce, Garlic", "", "starter")
                    },
        "lunch": {
             "Pasta": Recipe("Pasta", 2, 30, "Pasta, Tomatoes", "", "lunch")
        },
        "dessert": {
            "Icecream": Recipe("Icecream", 4, 60, "Cream, Strawberry", "", "dessert")
        }
    }