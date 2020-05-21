#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://krylov.cc/fansw.php?start=18540&sort_by_rate=0')
bs = BeautifulSoup(html.read(), 'html.parser')

