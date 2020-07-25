from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify,request,make_response
from flask_cors import cross_origin,CORS

# 設定DB連線
DB_host = "192.168.22.110"
DB_user = "root"
DB_passwd = "Pn123456"
DB_port = "3306"
DB_name = "Solartninc"

app = Flask(__name__)
CORS(app, resources=r'/*', supports_credentials=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + DB_user + ":"+ DB_passwd +"@"+ DB_host +":"+ DB_port +"/"+ DB_name
db = SQLAlchemy(app)

@app.route('/smtv', methods=['GET'])
def main_information():

    sql_cmd = """
        SELECT * from CronJob
        """
    query_data = db.engine.execute(sql_cmd)
    date = query_data.fetchall()
    result = [dict(row) for row in date]

    OnlinePeopleCommand = []
    RoomSchedulesNewAllGames = []
    SelfServerStatus = []
    GameScoreJson = []
    Daily_Cron = []
    RoomSchedulesLeagues = []
    RoomAccountNameSync = []
    SchedulesSports = []
    LeagueBoardJson = []
    RoomScheduleSyncStatus = []
    CalculateLevel = []
    WatchRecordCommandrunlive = []
    WatchRecordCommandrunvideo = []
    NewsSyncV2 = []
    OnlinePeopleCommandrunws = []
    OnlinePeopleCommandrunsolar_chat_sk = []
    Date = []

    for i in result:
        if i["CronJob"] == "OnlinePeopleCommand:runws_status":
            OnlinePeopleCommand.append(i["status_number"])
            Date.append(i["Date"])

        elif i["CronJob"] == "RoomSchedulesNewAllGames":
            RoomSchedulesNewAllGames.append(i["status_number"])

        elif i["CronJob"] == "SelfServerStatus":
            SelfServerStatus.append(i["status_number"])

        elif i["CronJob"] == "GameScoreJson":
            GameScoreJson.append(i["status_number"])

        elif i["CronJob"] == "Daily_Cron":
            Daily_Cron.append(i["status_number"])

        elif i["CronJob"] == "RoomSchedulesLeagues":
            RoomSchedulesLeagues.append(i["status_number"])

        elif i["CronJob"] == "RoomAccountNameSync":
            RoomAccountNameSync.append(i["status_number"])

        elif i["CronJob"] == "SchedulesSports":
            SchedulesSports.append(i["status_number"])

        elif i["CronJob"] == "LeagueBoardJson":
            LeagueBoardJson.append(i["status_number"])

        elif i["CronJob"] == "RoomScheduleSyncStatus":
            RoomScheduleSyncStatus.append(i["status_number"])

        elif i["CronJob"] == "CalculateLevel":
            CalculateLevel.append(i["status_number"])

        elif i["CronJob"] == "WatchRecordCommand:runlive":
            WatchRecordCommandrunlive.append(i["status_number"])

        elif i["CronJob"] == "WatchRecordCommand:runvideo":
            WatchRecordCommandrunvideo.append(i["status_number"])

        elif i["CronJob"] == "NewsSyncV2":
            NewsSyncV2.append(i["status_number"])

        elif i["CronJob"] == "OnlinePeopleCommand:runws":
            OnlinePeopleCommandrunws.append(i["status_number"])

        elif i["CronJob"] == "OnlinePeopleCommand:runsolar_chat_sk":
            OnlinePeopleCommandrunsolar_chat_sk.append(i["status_number"])
    result = {
        "OnlinePeopleCommand":OnlinePeopleCommand,
        "RoomSchedulesNewAllGames":RoomSchedulesNewAllGames,
        "SelfServerStatus":SelfServerStatus,
        "GameScoreJson":GameScoreJson,
        "Daily_Cron":Daily_Cron,
        "RoomSchedulesLeagues":RoomSchedulesLeagues,
        "RoomAccountNameSync":RoomAccountNameSync,
        "SchedulesSports":SchedulesSports,
        "LeagueBoardJson":LeagueBoardJson,
        "RoomScheduleSyncStatus":RoomScheduleSyncStatus,
        "CalculateLevel":CalculateLevel,
        "WatchRecordCommandrunlive":WatchRecordCommandrunlive,
        "WatchRecordCommandrunvideo":WatchRecordCommandrunvideo,
        "NewsSyncV2":NewsSyncV2,
        "OnlinePeopleCommandrunws":OnlinePeopleCommandrunws,
        "OnlinePeopleCommandrunsolar_chat_sk":OnlinePeopleCommandrunsolar_chat_sk,
        "Date":Date
    }

    response = jsonify(result)

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'

    return response



if __name__ == "__main__":
    app.run( host='192.168.25.17',port=5050, debug=True)

