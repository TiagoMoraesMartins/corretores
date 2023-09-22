from abc import ABC, abstractmethod
from app.models.entities.usuario_entity import Usuario
from typing import Type


class UsuarioInterface(ABC):
    """Interface UsuarioDAO"""

    @abstractmethod
    def cadastrar(self, usuario: Type[Usuario]) -> None:
        """abstractmethod"""

        raise Exception("abstractmethod not implemented")
