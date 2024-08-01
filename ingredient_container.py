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
        if quantity and quantity > 0: 
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