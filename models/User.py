from app import db, ma, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow import fields, validates_schema, ValidationError


class User(db.Model):
    """
    User model
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    _password = db.Column(db.String(128))
    profile_image = db.Column(db.String(128))
    user_ingredients = db.relationship('Ingredient', secondary='users_ingredients_table')

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')

    def __init__(self, data):
        for key, item in data.items():
            setattr(self, key, item)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def validate_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)


class UserSchema(ma.Schema):
    """
    User schema
    """

    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    password_confirmation = fields.String(required=True)
    user_ingredients = fields.Nested('IngredientSchema', many=True)

    @validates_schema
    def validate_password(self, data):
        if(data.get('password') != data.get('password_confirmation')):
            raise ValidationError(
                'Passwords do not match',
                'password_confirmation'
            )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'password_confirmation',
            'profile_image',
            'user_ingredients'
        )
