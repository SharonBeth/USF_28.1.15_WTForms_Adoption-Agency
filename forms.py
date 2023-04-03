"""Forms for the Adoption agency web page"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, URLField
from wtforms.validators import InputRequired, Email, Optional

species_choice = ["cat", "dog", "porcupine"]

class PetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired(message="Must enter pets name.")])

    species = SelectField('Species', choices=[(sp, sp) for sp in species_choice])

    photo_url = URLField("Must provide URL")

    age = IntegerField("age of the pet in Human years")

    notes = StringField("Any additional comments about the pet.")

    available = BooleanField("available?", default="checked")


class EditPetForm(FlaskForm):
    photo_url =URLField("Must provide URL")

    notes = StringField("Comments")

    available = BooleanField("Available?")
