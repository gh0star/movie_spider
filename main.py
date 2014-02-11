# coding:utf-8

import webapp2

import conf
from fetch import get_movie_dic, save_to_ndb
from mail import make_mail_content, send_mail
from movie import set_all_yes_movies

# Index Page Handler
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>Welcome To Movie Fetch For http://goxiazai.cc </h1>\
            <br/><h2>Name: lxstar<br/>Email: 362377891@qq.com</h2>')

# Fetch Movie Handler
class FetchHandler(webapp2.RequestHandler):
    def get(self):
        save_num = save_to_ndb(get_movie_dic())
        self.response.write('Fetch Job: movie number=%d'%save_num)

# Send Mail Handler
class MailHandler(webapp2.RequestHandler):
    def get(self):
        mail_result = ""
        content = make_mail_content()
        if content:
            send_mail(conf.MAIL_SENDER, conf.MAIL_TO, conf.MAIL_SUBJECT, content)
            mail_result = "send mail"
        else:
            mail_result = "no movie"
        self.response.write('Mail Job: %s'%mail_result)

#Debug Test Handler
class TestHandler(webapp2.RequestHandler):
    def get(self):
        set_all_yes_movies()
        self.response.write("test job")

# WSGI Enter Handler
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/fetch', FetchHandler),
    ('/mail', MailHandler),
    ('/test', TestHandler)
], debug=conf.DEBUG)
