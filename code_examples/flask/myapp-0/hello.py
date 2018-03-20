"""
My App 0: Hello with Bokeh plot.
"""
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from flask import Flask, Markup

app = Flask(__name__)

@app.route('/')
def hello():
    plot = figure()
    xdata = range(1, 6)
    ydata = [x*x for x in xdata]
    plot.line(xdata, ydata)

    return Markup(file_html(plot, CDN, "my plot"))

if __name__ == '__main__':
    app.run(debug=True)
