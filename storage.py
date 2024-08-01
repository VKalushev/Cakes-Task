from ingredient_container import IngredientContainer

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