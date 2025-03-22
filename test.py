from flask import Flask ,jsonify
import requests
response = requests.get("https://ayatblog.ir/date-time-api/time")
js = response.json()
app = Flask(__name__)

@app.route("/ali",methods=['GET'])
def ali():
    return jsonify(js)

if __name__ == "__main__":
    app.run(debug=True)