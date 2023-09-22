from enum import Enum


class TipoAcesso(Enum):
    """Definindo tipo de acesso"""

    ADMINISTRADOR = "administrador"
    FUNCIONARIO = "funcionário"


class TipoStatus(Enum):
    """Definindo tipo de status"""

    ATIVO = "ativo"
    INATIVO = "inativo"
    EXCLUIDO = "excluído"
