# coding:utf-8

from BeautifulSoup import BeautifulSoup
import conf
import urllib2
import hashlib
from movie import Movie

def get_movie_dic():
    movie_dic = []
    soup = BeautifulSoup(urllib2.urlopen(conf.FETCH_SITE))
    soup_movie = soup.findAll('div', attrs={'class': 'post'})

    for m in soup_movie:
        movie_dic.append({
                'name_md5': str(hashlib.md5(str(m.a.string)).hexdigest()),
                'name': str(m.a.string),
                'content': str(m.find("div", attrs={"class": "content"}).p),
                'info': str(m.find(id='infotb')),
                'href': str(m.a.get('href'))
            })
    return movie_dic

def save_to_ndb(movie_dic):
    save_num = 0

    for m in movie_dic:
        if Movie.query(Movie.name_md5 == m['name_md5']).count() == 0:
            Movie(
                    name_md5=m['name_md5'],
                    name=m['name'],
                    content=m['content'],
                    info=m['info'],
                    href=m['href'],
                    is_email='no'
                ).put()
            save_num += 1
            
    return save_num