from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    contact = db.Column(db.String(10))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    type_of_user = db.Column(db.String(50))


class Property(db.Model):
    __tablename__ = 'property'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip_code = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True))
    area = db.Column(db.Integer)
    number_bedrooms = db.Column(db.Integer)
    amenities = db.Column(db.String(255))
    furnish = db.Column(db.String(255))
    isAvailable = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class User_Property_Rel(db.Model):
    __tablename__ = 'property_user_rel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(255))
