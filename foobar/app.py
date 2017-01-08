from .bar import bar
from .foo import foo
from flask import Flask
app = Flask(__name__)

@app.route('/foo')
def get_foo():
    return foo()


@app.route('/bar')
def get_bar():
    return bar()
