from dataclasses import dataclass


@dataclass
class PropertyInfo:
    name: str
    value: int
    description: str
    createHeight: int
    updateHeight: int
