from dataclasses import dataclass

# si la clase no tiene fucniones y solo tiene datos es mejor usar un data class


@dataclass
class Cliente:
    cliente_id: int
    nombre: str
    edad: int
    email: str
