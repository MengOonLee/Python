from flask import Flask, jsonify

app = Flask(__name__)

@app.before_request
def before():
    print("Welcome to Flask")

@app.route('/<int:number>')
def incrementer(number):
    return jsonify(list(range(number))), 200

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
