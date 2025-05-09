from typing import List

from app.db import Database
from app.models import RecipeIngredient


# TODO: See https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries for passing parameters to queries

class RecipeIngredientRepository:
    def __init__(self, database):
        self.database = database

    def create_recipe_ingredient(self, recipe_id: int, ingredient_id: int, quantity: float) -> None:
        # TODO: challenge for you, insert a row into the recipe_ingredients table, where each row specifies the
        # TODO: required quantity of an ingredient for a recipe
        pass

    def get_recipe_ingredients(self, recipe_id: int) -> List[RecipeIngredient]:
        # TODO: your implementation here
        pass
