from flask import Flask, jsonify,request
import time
app = Flask(__name__);
@app.route("/bot")
def response():
#     query = dict(request.form)['query']
#     res = query + " " + time.ctime()
#     return jsonify({"response" : res})
      return "<h1>Welcome to Geeks for Geeks</h1>"
if __name__=="__main__":
    app.run()
