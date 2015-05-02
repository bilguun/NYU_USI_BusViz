###############################################################################
##
## index.py
## fimport Flask module and handle webserver requests
## by Renate Pinggera
##
###############################################################################


from flask import Flask
from flask import render_template
from flask_wtf import Form
from wtforms.fields.html5 import DateField
app = Flask(__name__)
app.secret_key = 'SHH!'
#define flask-wtforms
class ExampleForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')
    
## for DB access:
# from flask.ext.sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/bushistorical'
# db = SQLAlchemy(app)

@app.route('/')
def index():

    ## access Postgres DB
    ## quick and dirty first draft - TODO configure so we can also use localhost DBs
    ## research if Flask's SQLAlchemy module is better than psycopg2
    ## find file structure to separate DB config, queries and Python code

    ## Testing reading file from stop id
    # import read_1day_json 
 #        stop_id = "MTA_803008"
 #        stop_id_json = read_1day_json.readStopId(stop_id)
 #        print stop_id_json


    ################## PostGre Test ############################################
    ## TODO: Retrieve date from frontend input field
    date = "2014-08-04"

    #import psycopg2
    #date=raw_input('enter date: (2014-08-01)\n').strip()

    #commented for development
    #try:
    #   conn=psycopg2.connect("dbname='bushistorical' user='postgres' host='busvis.cloudapp.net'")
    #   cur=conn.cursor();
        # cur.execute("""SELECT COUNT(*)FROM(SELECT busid,COUNT(*) bus_count FROM bus_test WHERE to_char(TIMESTAMP,'YYYY-MM-DD') ='%s' GROUP BY busid) AS table1"""%(date))
    #   cur.execute("SELECT COUNT(DISTINCT busid) FROM bus_test")
    #   rows=cur.fetchall()
    #   totalBusCount = int(rows[0][0])

    #except:
        ## if not able to connect to DB use static fake number - TODO: change to error message
        # print '<html><body><p>could not connect to database</p></body></html>'
        #totalBusCount = 10000

    #new line after development - remove after finish
    totalBusCount = 10000

    ## send variable buscount to be shown inside /templates/index.html
    #return '<html><body><p>see what we got: ' + str(int(rows[0][0])) + '</p></body></html>'
    return render_template('result.html', date = date, buscount = totalBusCount)

@app.route('/query', methods=['POST','GET'])
def get_date():
    form = ExampleForm()
    if form.validate_on_submit():
        words="returning words from form"+form.dt.data.strftime('%Y-%m-%d')
        return render_template('result.html',date=words)#, date = form.dt.data.strftime('%Y-%m-%d'), buscount = 4545)
        # return form.dt.data.strftime('%Y-%m-%d')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    ## prod server:
    # app.run(host='0.0.0.0', port=5000, debug = True)

    ## localhost
    app.run(port=5000, debug = True)



