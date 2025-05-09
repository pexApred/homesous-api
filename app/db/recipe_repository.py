from typing import List

from app.db import Database
from app.models.recipe import Recipe


# TODO: See https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries for passing parameters to queries

class RecipeRepository:
    def __init__(self, database):
        self.database = database

    def create_recipe(self, name: str, instructions: str) -> Recipe:
        """Create a new recipe in the database."""
        inserted = self.database.query_for_first(
            """
            INSERT INTO recipes
                ( name
                , instructions
                )
            VALUES
                ( %(name)s
                , %(instructions)s
                ) RETURNING id, name, instructions
            """,
            {"name": name, "instructions": instructions}
        )

        return Recipe(
            id=inserted['id'],
            name=inserted['name'],
            instructions=inserted['instructions']
        )

    def get_recipe(self, id: int) -> Recipe:
        """Get a recipe by name."""
        result = self.database.query_for_first(
            """
            SELECT id, name, instructions
            FROM recipes
            WHERE id = %(id)s
            """,
            {"id": id}
        )

        if not result:
            return None

        return Recipe(
            id=result['id'],
            name=result['name'],
            instructions=result['instructions']
        )

    def get_all_recipes(self) -> List[Recipe]:
        """Get all recipes."""
        # TODO: your implementation here
