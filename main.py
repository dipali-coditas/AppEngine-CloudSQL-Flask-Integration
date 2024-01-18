import os
from flask_cors import CORS
from flask import Flask
import pymysql

app = Flask(__name__)

CORS(app)

connection = pymysql.connect(
    host=os.environ.get('CLOUD_SQL_CONNECTION_NAME'),
    port=int(os.environ.get('CLOUD_SQL_DATABASE_PORT')),
    user=os.environ.get('CLOUD_SQL_USERNAME'),
    password=os.environ.get('CLOUD_SQL_PASSWORD'),
    database=os.environ.get('CLOUD_SQL_DATABASE_NAME')
)
@app.route('/')
def func():
    with connection.cursor() as cursor:
        sql = "select demo_txt from demo_tbl;"
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.close()
        return result[0][0]