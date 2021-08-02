from flask import Flask, request,Response,jsonify,json
import requests
import mysql.connector
try:
    conn=mysql.connector.connect(
        host="localhost",
        password="",
        user="root",
        database="apiurl_db"
    )
    if conn.is_connected():
        print("database connected")
except:
    print("database not connected")

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=="GET":
        id=request.args.get("id")
        cur = conn.cursor()
        print(id)
        if id=="" or id ==None:
            cur.execute( "SELECT * FROM courses")
            result = cur.fetchall()
            return jsonify(message="success",data=result)
        else:
            cur.execute("SELECT * FROM courses  WHERE cid='%s'" % (id))
            result = cur.fetchall()
            return jsonify(message="success", data=result)


# @app.route('/index',methods=['GET','POST'])
# def index():
#     if request.method=="POST":
#             data={
#                 "data": [
#                     [
#                         1,
#                         "Datascience",
#                         2000,
#                         "all about data histograms "
#                     ],
#                     [
#                         2,
#                         "digital marketing",
#                         3000,
#                         "all about seo and smm and sem and content writing"
#                     ],
#                     [
#                         3,
#                         "uiux",
#                         1000,
#                         "all about designing the front end"
#                     ]
#                 ],
#                 "message": "success"
#             }
#             r=requests.post(url="http://127.0.0.1:5000/",data=data)
#             return json(r)

if __name__ == '__main__':
    app.run(debug=True)
