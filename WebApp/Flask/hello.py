from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'This is root page'

@app.route('/hello')
def hello():
    """Return a friendly HTTP greeting"""
    print('I am inside hello world')
    return 'Hello World!'

@app.route('/echo/<name>')
def echo(name):
    """echo <name>"""
    return f'Hello {name}'
  
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
