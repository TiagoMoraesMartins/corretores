# pylint: disable=E1101

from app import db
from app.enums import TipoAcesso, TipoStatus


class Usuario(db.Model):
    """Classe modelo de usuários"""

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    acesso = db.Column(
        db.String(50), default=TipoAcesso.FUNCIONARIO.value, nullable=False
    )
    status = db.Column(db.String(50), default=TipoStatus.ATIVO.value, nullable=False)
    imagem = db.Column(db.String(255), nullable=True)

    __slots__ = [
        "_id",
        "_nome",
        "_email",
        "_password",
        "_acesso",
        "_status",
        "_imagem",
    ]

    def __repr__(self):
        return f"Usuário email: {self.email},"
