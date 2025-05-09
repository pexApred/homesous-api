from flask import Flask

from app.db import init_db, IngredientRepository, RecipeRepository, RecipeIngredientRepository
from app.routes.ingredients import ingredients_bp, init_ingredients_routes
from app.routes.recipes import recipes_bp, init_recipes_routes


def create_app():
    app = Flask(__name__)

    # Initialize database connection
    database = init_db()
    database.connect()

    # Initialize repositories
    ingredient_repository = IngredientRepository(database)
    recipe_repository = RecipeRepository(database)
    recipe_ingredient_repository = RecipeIngredientRepository(database)

    # Initialize route handlers with repositories
    init_ingredients_routes(ingredient_repository)
    init_recipes_routes(recipe_repository, recipe_ingredient_repository)

    # Register blueprints
    app.register_blueprint(ingredients_bp)
    app.register_blueprint(recipes_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
