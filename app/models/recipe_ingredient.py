from dataclasses import dataclass
from typing import Optional

@dataclass
class RecipeIngredient:
    id: Optional[int]
    recipe_id: int
    ingredient_id: int
    quantity: float
    unit: str
    
    def __post_init__(self):
        # Ensure quantity is positive
        if self.quantity <= 0:
            raise ValueError("Ingredient quantity must be positive")