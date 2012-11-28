#! /usr/bin/env python
#-*-coding:utf-8-*-
import BeautifulSoup
import urllib2
import codecs
import os
URL='http://www.tetsudo.com/traffic/'
html=urllib2.urlopen(URL).read()
soup=BeautifulSoup.BeautifulSoup(html)
f=codecs.open('Traininfopy.cache','w','utf-8')
trableinfo=soup.findAll(id='hokai-1')[0].find('img').get('alt')
if(trableinfo!=u"○"):
    #f.write(u'道:')
    f.write(' ')
    f.write(soup.findAll(id='hokai-1')[0].findAll('td')[1].contents[0].contents[0])
    f.write('=')
    f.write(soup.findAll(id='hokai-1')[0].find('img').get('alt'))
    f.write(' ')
    f.close()
    os.system("cat Traininfopy.cache")
