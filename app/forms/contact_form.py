from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired('Por favor informe o nome')])
    email = StringField('E-mail', validators=[DataRequired('Por favor informe o e-mail'),Email('Por favor informe um e-mail válido')])
    subject = StringField('Assunto', validators=[DataRequired('Por favor informe o assunto')])
    message = TextAreaField('Mensagem', validators=[DataRequired('Por favor deixe uma mensagem')])
