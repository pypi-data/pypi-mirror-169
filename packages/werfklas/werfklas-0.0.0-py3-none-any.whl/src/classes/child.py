from flask_wtf import FlaskForm
from sqlalchemy.orm import Query
from wtforms import SubmitField, SelectField, HiddenField, StringField, DateField, BooleanField
from wtforms.validators import InputRequired, Length, Regexp

from src.classes.base import RearrangeDate
from src.classes.database import Family, sessionSetup

session = sessionSetup()
rearrange_date = RearrangeDate()


class AddChild(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    firstname = StringField('Voornaam', [InputRequired(),
                                         Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                         Length(min=2, max=25, message="Invalid sock name length")
                                         ])
    lastname = StringField('Achternaam', [InputRequired(),
                                          Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                          Length(min=2, max=25, message="Invalid sock name length")
                                          ])
    date_of_registration = DateField('Datum van inschrijving', [InputRequired()],
                                     format='%d-%m-%Y',
                                     render_kw={"placeholder": "dd-mm-jjjj"})
    parents = SelectField(u'Ouders', [InputRequired()],
                          coerce=int,
                          choices=Query([Family.id, Family.parent1 + ' ' + Family.lastname]).with_session(session))
    date_of_birth = DateField("Geboortedatum", [InputRequired()], format='%d-%m-%Y',
                              render_kw={"placeholder": "dd-mm-jjjj"})

    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('opslaan')


class EditChild(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    firstname = StringField('Voornaam', [InputRequired(),
                                         Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                         Length(min=2, max=25, message="Invalid sock name length")
                                         ])
    lastname = StringField('Achternaam', [InputRequired(),
                                          Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
                                          Length(min=2, max=25, message="Invalid sock name length")
                                          ])
    date_of_registration = DateField('Datum van inschrijving', [InputRequired()], format='%d-%m-%Y',
                                     render_kw={"placeholder": "dd-mm-jjjj"})
    parents = HiddenField()
    date_of_birth = DateField("Geboortedatum", [InputRequired()], format='%d-%m-%Y',
                              render_kw={"placeholder": "dd-mm-jjjj"})
    class_id = SelectField(u'Klas', coerce=int)
    redo_school_year = BooleanField(u'Schooljaar overdoen')
    # updated - date - handled in the route
    updated = HiddenField()
    submit = SubmitField('opslaan')
