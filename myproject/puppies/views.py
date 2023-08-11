from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm , DelForm


puppies_blueprint =Blueprint('puppies', __name__,
                             template_folder='templates/puppies')