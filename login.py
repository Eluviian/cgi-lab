#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

import os
import json
import secret 

from templates import login_page, secret_page, after_login_incorrect

s = cgi.FieldStorage()


username = s.getfirst("username")
password = s.getfirst("password")

print("Content-Type: text/html")
print()

if not username and not password:
    print(login_page())

elif username== secret.username and password== secret.password:
    print(secret_page(username, password))
else:
    print(login_page())
    print("username and password: ", username, password)