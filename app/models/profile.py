from app import db, random_words, login
from flask_login import UserMixin
from wtforms.validators import ValidationError

class Profile(db.Model):
    __tablename__ = "profile"

    # Profile information
    id = db.Column(db.Integer, primary_key=True, index=True)
    profile_picture_image_path = db.Column(db.String(64))
    description = db.Column(db.Text(1028))

    # Social media links
    twitter_link   = db.Column(db.String(128))
    facebook_link  = db.Column(db.String(128))
    instagram_link = db.Column(db.String(128))
    youtube_link   = db.Column(db.String(128))

    # Foreign key constraints
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))

    # Default attributes in a dict
    
    default_attributes = {
        "profile_picture_image_path": "",
        "description": "",
        "twitter_link": "",
        "instagram_link": "",
        "facebook_link": "",
        "youtube_link": ""
    }
    

    def set_attributes(self, new_attributes):
        """
        Updates the model from a dictionary of attribute names + values. If an attribute
        is passed into the dicitonary that doesn't exist on the model, then the model
        object won't be updated with that value

        >>> p = Profile()
        >>> attributes_to_update = {
        >>>     "twitter_link": "http://www.twitter.com/example-user",
        >>>     "profile_description": "This is my profile"
        >>>     "invalid_attribute": "won't be assigned"
        >>> }
        >>> p.set_attributes(attributes_to_update)
        >>> print(p.twitter_link)
        http://www.twitter.com/example-user
        >>> print(p.profile_description)
        This is my profile
        >>> print(p.invalid_attribute)
        AtributeError
        """        
        attributes_to_assign = self.default_attributes.copy()
        attributes_to_assign.update(
            {k: v for k, v in new_attributes.items() if k in self.default_attributes}
        )
        for attribute, value in attributes_to_assign.items():
            setattr(self, attribute, value)

    def __repr__(self):
        return f"<Profile {self.id}>"
