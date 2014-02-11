from google.appengine.ext import ndb

# Movie Model

class Movie(ndb.Model):
    name_md5 = ndb.StringProperty()
    name = ndb.StringProperty()
    content = ndb.StringProperty()
    info = ndb.StringProperty()
    href = ndb.StringProperty()
    is_email = ndb.StringProperty()

def get_no_movies():
    return Movie.query(Movie.is_email=="no")

def set_yes_movies(movies):
    for m in movies:
        m.is_email = "yes"
        m.put()

def set_all_yes_movies():
    for m in Movie.query():
        m.is_email = "no"
        m.put()