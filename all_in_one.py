from abc import ABC

class IngredientContainer(ABC):
    """
    Abstract base class for managing ingredients in a container.

    Attributes:
        ingredients (dict): Dictionary to store ingredients and their quantities.
    """

    def __init__(self):
        """Initialize an empty container of ingredients."""
        self.ingredients = {}

    def add_single_ingredient(self, name: str, quantity: int) -> None:
        """
        Add a single ingredient to the container.

        Args:
            name (str): The name of the ingredient.
            quantity (int): The quantity of the ingredient to add.
        """
        if quantity  and quantity > 0: 
            if name not in self.ingredients:
                self.ingredients[name] = quantity
            else:
                self.ingredients[name] += quantity

    def add_multiple_ingredients(self, ingredients: dict) -> None:
        """
        Add multiple ingredients to the container.

        Args:
            ingredients (dict): Dictionary of ingredients with their quantities.
        """
        for name, quantity in ingredients.items():
            self.add_single_ingredient(name, quantity)

    def get_ingredient_quantity(self, name: str) -> int:
        """
        Get the quantity of a specific ingredient.

        Args:
            name (str): The name of the ingredient.

        Returns:
            int: The quantity of the ingredient in the container.
        """
        return self.ingredients.get(name, 0)


class Recipe(IngredientContainer):
    """
    Class representing a recipe with required ingredients.

    Inherits from IngredientContainer.
    """

    def __init__(self, ingredients: dict = None):
        """
        Initialize the recipe with given ingredients.

        Args:
            ingredients (dict, optional): Dictionary of ingredients with their required quantities.
        """
        super().__init__()
        if ingredients:
            self.add_multiple_ingredients(ingredients)

    def __repr__(self):
        """Return a string representation of the recipe."""
        return f"Recipe({self.ingredients})"


class Storage(IngredientContainer):
    """
    Class representing a storage of available ingredients.

    Inherits from IngredientContainer.
    """

    def __init__(self, ingredients: dict = None):
        """
        Initialize the storage with given ingredients.

        Args:
            ingredients (dict, optional): Dictionary of ingredients with their available quantities.
        """
        super().__init__()
        if ingredients:
            self.add_multiple_ingredients(ingredients)

    def __repr__(self):
        """Return a string representation of the storage."""
        return f"Storage({self.ingredients})"


class Bakery:
    """
    Class containing methods to manage baking processes.
    """

    @staticmethod
    def cakes(recipe: Recipe, storage: Storage) -> int:
        """
        Calculate the maximum number of cakes that can be baked with the given recipe and storage.

        Args:
            recipe (Recipe): The recipe for the cakes.
            storage (Storage): The storage of available ingredients.

        Returns:
            int: The maximum number of cakes that can be baked.
        """
        min_cakes = float('inf')

        for ingredient_name, required_quantity in recipe.ingredients.items():
            available_quantity = storage.get_ingredient_quantity(ingredient_name)
            if available_quantity < required_quantity:
                return 0
            cakes_possible = available_quantity // required_quantity
            min_cakes = min(min_cakes, cakes_possible)

        return min_cakes



# recipe = Recipe({"apples": None, "flour": 300, "sugar": 150, "milk": 100, "oil":100})
# storage = Storage({"sugar": 500, "flour": 2000, "milk": 2000})
# storage.add_single_ingredient("oil", 100)

# bakery = Bakery()
# print(bakery.cakes(recipe, storage))

def cakes(recipe, available):
    bakery = Bakery()
    temp_recipe = Recipe(recipe)
    temp_storage = Storage(available)
    return bakery.cakes(temp_recipe,temp_storage)