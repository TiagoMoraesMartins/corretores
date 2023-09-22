from app import db
from app.models.entities.usuario_entity import Usuario
from app.controllers.interfaces.usuario_interface import UsuarioInterface
from app.models.services.usuario_service import UsuarioService
from type import Type


class UsuarioDAO(UsuarioInterface):
    """Classe de gerenciamento UsuarioDAO"""

    @classmethod
    def cadastrar(
        cls, usuario: Type[Usuario], usuario_service: Type[UsuarioService]
    ) -> None:
        """Insere os dados em Usuário
        :param - usuario
        """

        try:
            if usuario_service.validar_usuario(usuario):
                db.session.add(usuario)
            raise Exception("Não foi possível cadastrar o usuário!")

        except Exception as e:
            db.session.rollback()

        finally:
            db.session.commit()
