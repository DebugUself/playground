
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import BooleanField, StringField, PasswordField, validators

class FitForm(Form):
    m1 = StringField('m1',[validators.Length(min=0, max=25)])
    m2 = StringField('m2',[validators.Length(min=0, max=25)])
    m3 = StringField('m3',[validators.Length(min=0, max=25)])
    m4 = StringField('m4',[validators.Length(min=0, max=25)])
    m5 = StringField('m5',[validators.Length(min=0, max=25)])
    m6 = StringField('m6',[validators.Length(min=0, max=25)])
    m7 = StringField('m7',[validators.Length(min=0, max=25)])
    m8 = StringField('m8',[validators.Length(min=0, max=25)])
    m9 = StringField('m9',[validators.Length(min=0, max=25)])
    m10 = StringField('m10',[validators.Length(min=0, max=25)])
    fitdate = StringField('fitdate',[validators.Length(min=0, max=25)])

