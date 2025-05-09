from dataclasses import dataclass
from typing import Optional


@dataclass
class Ingredient:
    id: Optional[int]
    name: str
    quantity: float
    unit: str

    @property
    def is_available(self) -> bool:
        """Check if the ingredient is available (has quantity > 0)."""
        return self.quantity > 0
