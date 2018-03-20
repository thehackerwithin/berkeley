"""
My App 1: Hello with Bokeh plot and Jinja2 template.
"""
from bokeh.plotting import figure
from bokeh.embed import components
from flask import Flask, request, render_template, abort, Response

app = Flask(__name__)

@app.route('/')
def hello():
    plot = figure()
    plot.circle([1, 2], [3, 4])

    plot_script, plot_div = components(plot)
    kwargs = {'plot_script': plot_script, 'plot_div': plot_div}
    kwargs['title'] = 'hello'
    if request.method == 'GET':
        return render_template('hello.html', **kwargs)
    abort(404)
    abort(Response('Hello'))

if __name__ == '__main__':
    app.run(debug=True)
