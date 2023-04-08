from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/matches', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex = request.form['regex']
    matches = re.findall(regex, test_string)
    return render_template('matches.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)