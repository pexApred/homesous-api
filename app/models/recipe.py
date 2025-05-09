from dataclasses import dataclass
from typing import Optional


@dataclass
class Recipe:
    id: Optional[int]
    name: str
    instructions: str

    def __post_init__(self):
        # Ensure instructions is properly formatted
        if not self.instructions.strip():
            self.instructions = "No instructions provided."
