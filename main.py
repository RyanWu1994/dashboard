from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify,request



app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Pn123456@192.168.22.110:3306/17CE"
db = SQLAlchemy(app)


@app.route('/test')
def index():

    sql_cmd = """
        select * from main_information
        """
    query_data = db.engine.execute(sql_cmd)


    return jsonify({'result': [dict(row) for row in query_data]})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

