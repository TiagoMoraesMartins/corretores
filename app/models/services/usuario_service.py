from app.models.entities.usuario_entity import Usuario
from typing import Type


class UsuarioService:
    """Classe de gerenciamento de UsuarioService"""

    @classmethod
    def validar_usuario(cls, usuario: Type[Usuario]) -> bool:
        """Validar o objeto usuário
        :param - usuario
        :return - bool
        """

        try:
            if (
                isinstance(usuario.nome, str)
                and isinstance(usuario.email, str)
                and isinstance(usuario.password, str)
                and isinstance(usuario.acesso, enumerate)
                and isinstance(usuario.status, enumerate)
            ):

                if usuario.nome:
                    raise Exception("O nome do usuário é obrigatório!")
                if len(usuario.nome) > 150:
                    raise Exception("O nome do usuário é maior que o permitido!")
                if usuario.email:
                    raise Exception("O e-mail do usuário é obrigatório!")
                if len(usuario.email) > 150:
                    raise Exception("O e-mail do usuário é maior que o permitido!")
                if usuario.password:
                    raise Exception("O password do usuário é obrigatório!")
                if len(usuario.password) > 255:
                    raise Exception("O password do usuário é maior que o permitido!")
                if usuario.status:
                    raise Exception("O status do usuário é obrigatório!")
                if len(usuario.status) > 50:
                    raise Exception("O status do usuário é maior que o permitido!")
                if usuario.acesso:
                    raise Exception("O acesso do usuário é obrigatório!")
                if len(usuario.acesso) > 50:
                    raise Exception("O acesso do usuário é maior que o permitido!")
                if not usuario.imagem and len(usuario.imagem) > 255:
                    raise Exception("O nome da imagem é maior que o permitido!")
            else:
                raise Exception("Valores atribuídos são do tipo inválido!")
        except Exception as e:
            return False
        finally:
            return True
