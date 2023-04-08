from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def Home():
    return 'Welcome'
@app.route('/up')
def up():
    a = request.args.get('a')
    return a.upper()
if __name__ == '__main__':
    app.run(debug=True)