from dataclasses import dataclass


@dataclass
class Producto:
    product_id: int
    nombre: str
    descripcion: str
