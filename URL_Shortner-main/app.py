import os
from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms import validators
import string
from random import choice

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
Migrate(app, db)

class Url(db.Model):
    __tablename__='links'
    id= db.Column(db.Integer, primary_key= True)
    long_url= db.Column(db.Text)
    short_url= db.Column(db.Text)

    def __init__(self,long_url,short_url):
        self.long_url= long_url
        self.short_url= short_url

def shortURL(charlen):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(charlen))

@app.route('/',methods=["GET","POST"])
def home_page():
    if request.method=="POST":
        long_URL= request.form['url'] 
        currentUrl = Url.query.filter_by(long_url=long_URL).first()
        if currentUrl:
            return render_template('home.html', error=0, finalurl=currentUrl.short_url)
        else:
            if validators.url(long_URL):
                while True:
                    shortLink = shortURL(3)
                    short_url = Url.query.filter_by(short_url=shortLink).first()
                    if not short_url:
                        lnk=Url(long_URL,shortLink)
                        db.session.add(lnk)
                        db.session.commit()
                        return render_template('home.html',error=0,finalurl=shortLink)
            else:
                return render_template('home.html',error=1)
    return render_template("home.html")

@app.route('/history',methods=["GET","POST"])
def history_page():
    lnks=Url.query.all()
    return render_template("history.html",hist=lnks)

@app.route('/<finalurl>')
def redirection(finalurl):
    fullurl = Url.query.filter_by(short_url=finalurl).first()
    if fullurl:
        return redirect(fullurl.long_url)
    else:
        return f"<h1>URL doesn't Exist</h1>"

@app.route('/delete/<int:id>')
def delete(id):
    item = Url.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/history')

if __name__=="__main__":
    app.run(debug=True)