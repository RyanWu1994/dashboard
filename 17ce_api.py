from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify,request,make_response
from flask_cors import cross_origin,CORS

# 設定DB連線
DB_host = "192.168.22.110"
DB_user = "root"
DB_passwd = "Pn123456"
DB_port = "3306"
DB_name = "17CE"

app = Flask(__name__)
CORS(app, resources=r'/*', supports_credentials=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + DB_user + ":"+ DB_passwd +"@"+ DB_host +":"+ DB_port +"/"+ DB_name
db = SQLAlchemy(app)

# 电信 Telecom
@app.route('/Telecom', methods=['GET'])
def main_information_Telecom():

    sql_cmd = """
        SELECT * from main_information WHERE URL = 'smtv.io' AND Line = '电信' AND DATE > '2020-07-28'
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

#-----------------------------------------------------------------------
# 联通 Unicom
@app.route('/Unicom', methods=['GET'])
def main_information_Unicom():

    sql_cmd = """
        SELECT * from main_information WHERE URL = 'smtv.io' AND Line = '联通' AND DATE > '2020-07-28'
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

#-----------------------------------------------------------------------
# 移动 mobile
@app.route('/mobile', methods=['GET'])
def main_information_mobile():

    sql_cmd = """
        SELECT * from main_information WHERE URL = 'smtv.io' AND Line = '移动' AND DATE > '2020-07-28'
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

#-----------------------------------------------------------------------
# 海外 overseas
@app.route('/overseas', methods=['GET'])
def main_information_overseas():

    sql_cmd = """
        SELECT * from main_information WHERE URL = 'smtv.io' AND Line = '海外' AND DATE > '2020-07-28'
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

#-----------------------------------------------------------------------
# 教育网 Education 
@app.route('/Education', methods=['GET'])
def main_information_Education():

    sql_cmd = """
        SELECT * from main_information WHERE URL = 'smtv.io' AND Line = '教育网' AND DATE > '2020-07-28'
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

#-----------------------------------------------------------------------
# 台湾 Taiwan
@app.route('/Taiwan', methods=['GET'])
def main_information_Taiwan():

    sql_cmd = """
        SELECT * from main_information WHERE URL = 'smtv.io' AND Line = '台湾' AND DATE > '2020-07-28'
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


if __name__ == "__main__":
    app.run( host='192.168.25.14',port=5000, debug=True)
