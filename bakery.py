from storage import Storage
from recipe import Recipe

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