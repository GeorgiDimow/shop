from app import db, login
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash


class Client(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=True)
    last_name = db.Column(db.String(64), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    orders = db.relationship('Order', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Client {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return Client.query.get(int(id))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(140))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    def __repr__(self):
        return '<Order {}>'.format(self.body)