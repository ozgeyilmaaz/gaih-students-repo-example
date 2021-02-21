class Cooking:

    def cook(self):
        print("The fire of the stove is turned on.")
        print("Food is placed on the stove.")

    def mixing(self):
        print("The mixing process is carried out.")

    def throw_salt(self):
        print("Salt is added.")

    def service(self):
        print("It is taken to the plate to be served after it is cooked.")
        print("Enjoy your meal!")


class Recipe1(Cooking):

    def __init__(self, category, name, time):
        super().__init__()
        self.category = category
        self.name = name
        self.time = time

    def ingredient(self):
        name = "OMELETTE"
        print(name, "RECIPE")
        print("---------------")
        products = ["egg", "butter", "cheese", "salt"]
        self.products = products

    def info(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}.")
        print(f"The cooking time: {self.time}")
        print()
        print("INGREDIENTS:")
        print(f"1 {self.products[0]}, 30 g {self.products[1]}, 60 g {self.products[2]}, 1 teaspoon {self.products[3]}")
        print()

    def prepare(self):
        print("PREPERATION:")
        print("Egg breaks into a bowl.")
        print("Cheese added to the bowl.")


class Recipe2(Cooking):

    def __init__(self, category, name, time):
        super().__init__()
        self.category = category
        self.name = name
        self.time = time

    def ingredient(self):
        name = "CREPE"
        print(name, "RECIPE")
        print("--------------")
        products = ["egg", "flour", "milk", "salt"]
        self.products = products

    def info(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}.")
        print(f"The cooking time: {self.time}")
        print()
        print("INGREDIENTS:")
        print(f"2 {self.products[0]}, 1 glass of {self.products[1]}, 1 glass of {self.products[2]}, " +
              f"1 teaspoon {self.products[3]}")
        print()

    def prepare(self):
        print("PREPERATION:")
        print("Eggs are broken into a large bowl.")
        print("Flour and milk are also added in desired amounts.")


class Recipe3(Cooking):

    def __init__(self, category, name, time):
        super().__init__()
        self.category = category
        self.name = name
        self.time = time

    def ingredient(self):
        name = "FRIED POTATOES"
        print(name, "RECIPE")
        print("-------------------")
        products = ["potato", "oil", "salt"]
        self.products = products

    def info(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}.")
        print(f"The cooking time: {self.time}")
        print()
        print("INGREDIENTS:")
        print(f"2 {self.products[0]}, 1 glass of {self.products[1]}, 1 teaspoon {self.products[2]}")
        print()

    def prepare(self):
        print("PREPERATION:")
        print("The potatoes are peeled.")
        print("It is thinly sliced.")
        print("It is put into the pot with the oil.")


omelette = Recipe1("Breakfast", "Omelette", "15 minutes")
omelette.ingredient()
print(omelette.info())
print(omelette.prepare())
print(omelette.throw_salt())
print(omelette.mixing())
print(omelette.cook())
print(omelette.service())
print()

crepe = Recipe2("Breakfast", "Crepe", "40 minutes")
crepe.ingredient()
print(crepe.info())
print(crepe.prepare())
print(crepe.throw_salt())
print(crepe.mixing())
print(crepe.cook())
print(crepe.service())
print()

fried_potatoes = Recipe3("Snack", "Fried Potatoes", "25 minutes")
fried_potatoes.ingredient()
print(fried_potatoes.info())
print(fried_potatoes.prepare())
print(fried_potatoes.throw_salt())
print(fried_potatoes.cook())
print(fried_potatoes.mixing())
print(fried_potatoes.service())
