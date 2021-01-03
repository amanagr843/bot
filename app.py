from flask import Flask, jsonify,request
import time
<<<<<<< HEAD
app = Flask(__name__)
@app.route("/bot", methods=["POST"])
=======
app = Flask(__name__);
@app.route("/bot/",methods=['POST'])
>>>>>>> f932b467917090f453884869dcfa62f099dd4fac
def response():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {param} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })
if __name__=="__main__":
    app.debug = True
    app.run()
