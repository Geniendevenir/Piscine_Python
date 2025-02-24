import sys

def cooking():
    Cookbook = {
        "Sandwich": {
        'ingredients': (['ham', 'bread', 'cheese' 'tomatoes']),
        'meal': 'lunch',
        'prep_time': 10
        },
        "Cake": {
        'ingredients':(['flour', 'sugar', 'eggs']),
        'meal':'desert',
        'prep_time':60
        },
        "Salad": {
        'ingredients':(['avocado', 'arugula', 'tomatoes', 'spinach']),
        'meal':'lunch',
        'prep_time':15
        }
    }
    print("Welcome to the Python Cookbook !")
    while True:
        print("\nList of available options:")
        print("\n1: Add a recipe")
        print("\n2: Delete a recipe")
        print("\n3: Print a recipe")
        print("\n4: Print the Cookbook")
        print("\n5: Quit")
        while True:
            while True:
                try:
                    choice = int(input("\n\nPlease select an option:\n"))
                    break
                except:
                    print("Error: Choice Input must be between 1 and 5")
            if choice <= 0 or choice > 5:
                print("Error: Choice Input must be between 1 and 5")
            else:
                break
        if choice == 1:
            add_recipe(Cookbook)
        elif choice == 2:
            rec_to_del = input("What is the name of the recipe you would like to Delete?:")
            del_recipe(Cookbook, rec_to_del)
        elif choice == 3:
            rec_to_print = input("What is the name of the recipe you would like to Print?:")
            try:
                print_details(Cookbook[rec_to_print])
            except:
                print("Error: No recipe of this name are currently in the Cookbook")
        elif choice == 4:
            print_recipe(Cookbook)
        else:
            print("Cookbook closed. Goodbye !")
            break

def print_recipe(Cookbook):
    for key in Cookbook:
        print(key)

def print_details(recipe):
    try:
        print(recipe)
    except:
        print("Error: No recipe of this name are currently in the Cookbook")

def del_recipe(Cookbook, recipe):
    try:
        del Cookbook[recipe]
    except:
        print("Error: No recipe of this name are currently in the Cookbook")

def add_recipe(Cookbook):
    name = input("Enter a name: ")
    ingredients = input("Enter ingredients: ").split(", ")
    meal = input("Enter meal type: ")
    while True:
        try:
            time = int(input("Enter a preparation time: "))
            break
        except:
            print("Error: prep_time Input must be a valid integer")
    Cookbook[name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': time}
    print_details(Cookbook[name])

cooking()
