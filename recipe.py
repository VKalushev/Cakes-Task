from ingredient_container import IngredientContainer

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