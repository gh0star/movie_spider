#coding:utf-8

import jinja2
import os
from movie import get_no_movies, set_yes_movies

from google.appengine.api import mail

def send_mail(sender, to, subject, body):
    msg = mail.EmailMessage(sender=sender,subject=subject,to=to)
    msg.html = body
    msg.send()

def make_mail_content():
    JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)
    movies = get_no_movies()
    if movies.count() > 0:

        template = JINJA_ENVIRONMENT.get_template('mail.html')
        t_render = template.render({
                'movies': movies
            })
        set_yes_movies(movies)
    else:
        t_render = None
    return t_render
