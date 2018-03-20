"""
My App 2: Hello with Bokeh plot, Jinja2 template, and Bootstrap
"""
from bokeh.plotting import figure
from bokeh.embed import components
from flask import (
    Flask, request, render_template, abort, Response, redirect, url_for
)
import requests
import pandas as pd
import future
from io import StringIO

app = Flask(__name__)

URL = 'https://developer.nrel.gov/api/pvdaq/v3/site_data'


@app.route('/', methods=['GET', 'POST'])
@app.route('/<apikey>/<int:stationid>/<startdate>/<enddate>/<aggregate>',
           methods=['GET', 'POST'])
def hello(apikey=None, stationid=1230, startdate='9/1/2002',
          enddate='9/1/2007', aggregate='daily'):
    if request.method == 'GET':
        kwargs = {'title': 'NREL PVDAQ'}
        if apikey is not None:
            params = {'api_key': apikey}
            params.update(
                station_id=stationid, start_date=startdate, end_date=enddate,
                limit_fields='energy_from_array, poa_irradiation',
                aggregate=aggregate
            )
            try:
                r = requests.get('%s.json' % URL, params=params)
            except Exception:
                pass
            else:
                if r.ok:
                    outputs = r.json()['outputs']
                    headers, outputs = outptus[0], outputs[1:]
                    data = {h: dat for h, dat in zip(headers, zip(*outputs))}
                    df = pd.DataFrame(data)
                    df = df.set_index('measdatetime')
                    plot = figure(title='station id: %d' % stationid,
                                  x_axis_type="datetime")
                    dt = df.index.to_datetime()
                    for h in headers:
                        plot.line(dt, df[h], legend=h)
                    plot_script, plot_div = components(plot)
                    kwargs.update(plot_script=plot_script, plot_div=plot_div)
        return render_template('hello.html', **kwargs)
    elif request.method == 'POST':
        apikey = request.form.get('apikey')
        stationid = request.form.get('stationid', 1230)
        startdate = request.form.get('startdate', '9/1/2002')
        enddate = request.form.get('enddate', '9/1/2007')
        aggregate = request.form.get('aggregateFormControlSelect', 'daily')
        comma_seperated = request.form.get('commaSeparatedCheck')
        if comma_seperated:
            params = {'api_key': apikey}
            params.update(
                station_id=stationid, start_date=startdate, end_date=enddate,
                limit_fields='energy_from_array, poa_irradiation',
                aggregate=aggregate
            )
            try:
                r = requests.get('%s.csv' % URL, params=params)
            except Exception:
                pass
            else:
                if r.ok:
                    f = StringIO(r.content.decode('utf-8'))
                    return send_file(
                        f, attachment_filename="%s.txt" % stationid,
                        as_attachment=True
                    )
        kwargs = {'apikey': apikey, 'stationid': stationid,
                  'startdate': startdate, 'enddate': enddate,
                  'aggregate': aggregate}
        return redirect(url_for('hello', **kwargs))
    abort(404)
    abort(Response('Hello'))


if __name__ == '__main__':
    app.run(debug=True)
