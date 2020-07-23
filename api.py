from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify,request,make_response
from flask_cors import cross_origin,CORS

# 設定DB連線
DB_host = "192.168.0.19"
DB_user = "root"
DB_passwd = "Pn123456"
DB_port = "3306"
DB_name = "17CE"

app = Flask(__name__)
CORS(app, resources=r'/*', supports_credentials=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + DB_user + ":"+ DB_passwd +"@"+ DB_host +":"+ DB_port +"/"+ DB_name
db = SQLAlchemy(app)

@app.route('/Telecom', methods=['GET'])
def main_information():

    sql_cmd = """
        SELECT * from main_information WHERE URL = 'smtv.io' AND Line = '电信' AND DATE > date_sub(now(), INTERVAL 3 HOUR)
        """
    query_data = db.engine.execute(sql_cmd)
    date = query_data.fetchall()
    Date = []
    Line = []
    Fastest_node = []
    Fastest_node_seconds = []
    Slowest_node = []
    Slowest_node_seconds = []
    Average_response = []

    for i in range(len(date)):
        for index,content in enumerate(date[i]):
            if index == 0:
                URL = content
            elif index == 1:
                Date.append(content)
            elif index == 2:
                Line.append(content)
            elif index == 3:
                Fastest_node.append(content)
            elif index == 4:
                Fastest_node_seconds.append(content)
            elif index == 5:
                Slowest_node.append(content)
            elif index == 6:
                Slowest_node_seconds.append(content)
            elif index == 7:
                Average_response.append(content)

    response = {
        "URL":URL,
        "Line":Line,
        "Date":Date,
        "Fastest_node":Fastest_node,
        "Fastest_node_seconds":Fastest_node_seconds,
        "Slowest_node":Slowest_node,
        "Slowest_node_seconds":Slowest_node_seconds,
        "Average_response":Average_response
    }
    response = make_response(jsonify(response))

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'

    return response



@app.route('/node_information', methods=['GET'])
def node_information():

    sql_cmd = """
        select * from node_information WHERE DATE > date_sub(now(), INTERVAL 1 hour)
        """
    query_data = db.engine.execute(sql_cmd)

    result = [dict(row) for row in query_data]
    response = make_response(jsonify({"result":result}))

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'


    return response

if __name__ == "__main__":
    app.run( host='192.168.0.12',port=5050, debug=True)

