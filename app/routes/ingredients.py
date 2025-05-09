from flask import Blueprint, request, jsonify
from app.db.ingredient_repository import IngredientRepository

ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')
ingredients_repository = None

def init_ingredients_routes(repository):
    global ingredients_repository
    ingredients_repository = repository


@ingredients_bp.route('', methods=['GET'])
def get_ingredients():
    """Get all ingredients."""
    ingredients = ingredients_repository.get_all_ingredients()
    return jsonify([{
        'id': ingredient.id,
        'name': ingredient.name,
        'quantity': ingredient.quantity,
        'unit': ingredient.unit,
    } for ingredient in ingredients])


@ingredients_bp.route('', methods=['POST'])
def add_ingredient():
    """Add a new ingredient."""
    data = request.json

    if not all(key in data for key in ['name', 'quantity', 'unit']):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Create ingredient
        ingredient = ingredients_repository.create_ingredient(
            name=data['name'],
            quantity=float(data['quantity']),
            unit=data['unit'],
        )

        return jsonify({
            'id': ingredient.id,
            'name': ingredient.name,
            'quantity': ingredient.quantity,
            'unit': ingredient.unit,
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@ingredients_bp.route('/<int:ingredient_id>', methods=['GET'])
def get_ingredient_by_id(ingredient_id):
    """Get an ingredient by ID."""
    # TODO: your implementation here


@ingredients_bp.route('/<int:ingredient_id>/quantity', methods=['PATCH'])
def update_quantity(ingredient_id):
    """Update an ingredient's quantity."""
    # TODO: your implementation here
