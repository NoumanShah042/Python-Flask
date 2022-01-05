from datetime import datetime  

from flaskblog import db    # circular import  ( cannot import name 'User' from partially initialized module 'models' )
# from __main__ import db   # cannot import name 'db' from '__main__' 

# ************

# when we run python script(file) directly from the python cmd, python calls the
# name of only that  script  __main__ , so the current name of file is undefined 

# wo flaskblog ko janta hi nhi (because of direct run ), is liye wo dobara ise run krta ha
# lekin wo __main__ ko janta ha is liye usi jaga error deta ha

# lekin jb wo 2osri dfa flaskblog run krta ha tw , wo models file ko janta ha , 
# because k wo direct run nhi hoi , or error de deta ha k ye partially initialized module ha.


# ************


class User(db.Model):   # this type of class also called a model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    # it says that it has relationship with Post Model
    # backref here is similar to adding another column in Post Model,
    #    so we can access user-object by using post-object as *** post_obj.author ***
    #    which do not have in Post-Model
    # now by using posts attribute we can access all the posts created by the individual user.
    # this is a relationship and not the column , it run additional query in background to do its job
    # we can access posts of individual user by using obj.posts ( obj - object of User Model)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # to specify the user in the post model we have user_id for the author
    # same type as the primary key of the User Model (user.id)
    # nullable=False says that each post must have an author
    # we also provide user id , of User object, for creating Post object of that user
    # here we can use similar id with more than one 1 Post Object

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
