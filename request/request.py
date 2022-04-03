from flask import Flask, request
import requests
import json

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sbb_profile_data'

mysql = MySQL(app)


@app.route('/data', methods=["POST"])
def post():
    data = request.get_json()
    cur = mysql.connection.cursor()
    try:
        cur.execute(
            "INSERT INTO tbl_sbb_data (cardid) VALUES (" + str(data["CardId"]) + ")")
    except:
        print("Error")
    mysql.connection.commit()
    cur.close()

    return str(cur.lastrowid)


@app.route('/data', methods=["GET"])
def get():
    cur = mysql.connection.cursor()
    cur.execute("SELECT cardid FROM tbl_sbb_data")
    rv = cur.fetchall()
    response = []
    for row in rv:
        response.append({"CardId": row[0]})
    return app.response_class(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )


app.run(host='0.0.0.0')
