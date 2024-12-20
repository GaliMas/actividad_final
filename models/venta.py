from dataclasses import dataclass


@dataclass
class Venta:
    venta_id: int
    producto_id: int
    cliente_id: int
    importe: float
