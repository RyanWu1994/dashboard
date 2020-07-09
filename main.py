from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify,request,make_response
from flask_cors import cross_origin,CORS



app = Flask(__name__)

CORS(app, resources=r'/*', supports_credentials=True)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Pn123456@192.168.22.110:3306/17CE"
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
# @cross_origin()
def index():

    sql_cmd = """
        select * from main_information
        """
    query_data = db.engine.execute(sql_cmd)

    result = [dict(row) for row in query_data]
    response = make_response(jsonify({"result":result}))

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    # rst = make_response(query_data)
    # rst.headers['Access-Control-Allow-Origin'] = '*'

    return response

if __name__ == "__main__":
    app.run(port=5000, debug=True)

