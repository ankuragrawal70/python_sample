from itertools import *
# print("xcd".startswith(("a", "xc")))

f = lambda x: "yes" if x.startswith(("a", "xc")) else "No"
print(f('xcd'))


from flask import Flask

app = Flask(__name__)
app.run()

from flask import request

from flask_restful import Resource, Api