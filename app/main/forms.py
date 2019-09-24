from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required
from flask_login import current_user

class CreateBlog(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    comment = StringField('Comment')
    submit = SubmitField('Post')