from flask import Flask, render_template, flash, redirect, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

# from forms import AddSnackForm
# from forms import UserForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# debug = DebugToolbarExtension(app)
# 
app.app_context().push()
connect_db(app)
db.create_all()

@app.route("/", methods=["GET", "POST"])
def homepage():
    """Show adoption main page that will display all pets available for adoption."""

    pets = Pet.query.filter(Pet.available==True).all()
    return render_template("main_page.html", pets=pets)

@app.route('/pet-form/new', methods=["GET", "POST"])
def enter_new_pet():
    """Form to enter a new pet to the the pet adoption center"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("pet-form.html", form=form)

@app.route('/pet/<int:pet_id>', methods=["GET", "POST"])
def pet_detail_page(pet_id):
    """Shows details of chosen pet from main adoption page"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data

        db.session.commit()
        return redirect("/")
    else:
        return render_template("pet_details.html", form=form, pet=pet)