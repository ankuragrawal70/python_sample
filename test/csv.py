from flask_restful import reqparse
from flask import jsonify
from flask.views import View, MethodView
from flask import render_template
from django.forms import Form
from exceptions import ValueError
import asyncore

import cx_Oracle
c = cx_Oracle.connect()
c.rollback()

import fabric

from django.db import transaction
transaction.atomic()
from threading import Thread
import gevent
from gevent import Greenlet
import paramiko

a = Greenlet()

# cx_Oracle.makedsn()
# str.replace()
# import traceback
# traceback.format_exc()
from flask import url_for
#
# import traceback
# traceback.format_exc()
#
# from datetime import datetime, date
# print(date.__eq__())
# print(datetime.today().date())
#
# import subprocess
# import sys, errno
#
# import os
# os.makedirs()
# l = ['av', 'x']
# l.reverse()
# import fileinput
from filelock import FileLock
import subprocess
# print(subprocess.call("echo Hello World!", shell=True))

# import re
# re.match()
# re.sub()
#
# "".join()
#subprocess.check_output(["echo", "Hello World!"])

# from collections import deque
# p=subprocess.Popen(('python', 'iter.py'))
# print(p.communicate())
# p=subprocess.Popen('python iter.py', shell=True)
# # p.communicate()
# # subprocess.call("python iter.py", shell=True)
#
# #
# # import functools
# #
# # import cx_Oracle
# # d= cx_Oracle.connect()
# #
# import os
# os.fork()

ssh = paramiko.SSHClient()
ssh.connect()
ssh.exec_command()