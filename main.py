import pymysql as pymysql
from flask import *

app = Flask(__name__)


# your routes
# create a database named api
# create a table named locations
# location_id INT  Ai PK,
# lat VARCHAR
# log VARCHAR
# name VARCHAR
# phone  VARCHAR
# desc VARCHAR
@app.route('/api/all')
def all():
    con = pymysql.connect(host="localhost", user='root', password='', database='location')
    cursor = con.cursor(pymysql.cursors.DictCursor)
    sql = "select * from location"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)


# practice
# create news table
# colums
# news id
# tittle varchar
# descc varchar
# author varchar


if __name__ == "__main__":
    app.run()
