from app.db import Database
from app.models.ingredient import Ingredient


# TODO: See https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries for passing parameters to queries

class IngredientRepository:
    def __init__(self, database):
        self.database = database

    def create_ingredient(self, name: str, quantity: float, unit: str) -> Ingredient:
        """Create a new ingredient in the database."""
        inserted = self.database.query_for_first(
            query="""
                  INSERT INTO ingredients
                      ( name
                      , quantity
                      , unit
                      )
                  VALUES
                      ( %(name)s
                      , %(quantity)s
                      , %(unit)s
                      ) RETURNING id, name, quantity, unit, expiry_date
                  """,
            params={"name": name, "quantity": quantity, "unit": unit}
        )[0]

        return Ingredient(
            id=inserted['id'],
            name=inserted['name'],
            quantity=inserted['quantity'],
            unit=inserted['unit']
        )

    def get_ingredient(self, id: int) -> Ingredient:
        """Get an ingredient by ID."""
        result = self.database.query_for_first(
            """
            SELECT id, name, quantity, unit
            FROM ingredients
            WHERE id = %(id)s
            """,
            {"id": id}
        )

        if not result:
            return None

        return Ingredient(
            id=result['id'],
            name=result['name'],
            quantity=result['quantity'],
            unit=result['unit'],
        )

    def update_ingredient_quantity(self, ingredient_id: int, quantity_change: float) -> Ingredient:
        """Update an ingredient's quantity by adding the specified amount (can be negative)."""
        # TODO: your implementation here, see above examples
        pass

    def get_all_ingredients(self) -> list[Ingredient]:
        """Get all ingredients."""
        # TODO: your implementation here, see above examples
        pass
