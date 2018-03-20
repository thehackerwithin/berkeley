"""
My App 2: Hello with Bokeh plot, Jinja2 template, and Bootstrap
"""
from bokeh.plotting import figure
from bokeh.embed import components
from flask import (
    Flask, request, render_template, abort, Response, redirect, url_for
)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/<xdata>', methods=['GET', 'POST'])
def hello(xdata=None):
    if request.method == 'GET':
        kwargs = {'title': 'hello'}
        if xdata is not None:
            try:
                xdata = [float(x) for x in xdata.split(',')]
            except ValueError:
                pass
            else:
                plot = figure(title='squares from input')
                plot.line(xdata, [x*x for x in xdata], legend='y=x^2')
                plot_script, plot_div = components(plot)
                kwargs.update(plot_script=plot_script, plot_div=plot_div)
        return render_template('hello.html', **kwargs)
    elif request.method == 'POST':
        xdata = request.form.get('xdata')
        comma_seperated = request.form.get('commaSeparatedCheck')
        if not comma_seperated:
            xdata = ','.join(xdata.split())
        return redirect(url_for('hello', xdata=xdata))
    abort(404)
    abort(Response('Hello'))


if __name__ == '__main__':
    app.run(debug=True)
