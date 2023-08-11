# MODELS.PY


from myproject import db
class Puppy(db.Model):

    __tablename__ ='puppies'
    id =db.Column(db.Integer , primary_key=True)
    name=db.Column(db.Text)
    owner=db.relationship('Owner', backref='puppy',uselist=False)

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner}"
        else:
           return f"Puppy name is {self.name} and has no owner assigned"
        
class Owner(db.Model):

    __tablename__ ='owners'
    id =db.Column(db.Integer , primary_key=True)
    name=db.Column(db.Text)