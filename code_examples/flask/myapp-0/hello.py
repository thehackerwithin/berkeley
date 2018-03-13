"""
My App 1: Hello with Bokeh plot.
"""
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from flask import Flask, Markup

app = Flask(__name__)

@app.route('/')
def hello():
    plot = figure()
    plot.circle([1, 2], [3, 4])

    return Markup(file_html(plot, CDN, "my plot"))

if __name__ == '__main__':
    app.run(debug=True)
