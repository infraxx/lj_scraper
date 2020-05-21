#!/usr/bin/python3

from lj import lj as _lj

ljclient = _lj.LJServer("Python-Blog3/1.0", "http://daniil-r.ru/bots.html; i@daniil-r.ru")
login_info = ljclient.login("***", "***")
# print(login_info)
events = ljclient.getevents_day(2012, 8, 19)
print(events)
