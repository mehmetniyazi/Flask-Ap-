from flask import Flask,render_template,jsonify,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/CapstoneApp/logdata.db'
db = SQLAlchemy(app)
@app.route("/")

def index(): 
    numbers=[1,2,1,10]
    message="Bu bir messaj dır"
    
    return render_template("index.html",numbers=numbers)


@app.route("/add",methods=["POST"])
def searchforItem():
    title=request.form.get("item")
    print(title)
    try: 
        associations=assocs.query.filter(assocs.itemA==title)
    except:
        associations=[]
    son=[]
    first=1
    for i in associations:
        assoc=[i.itemA,i.itemB,i.freqA,i.supportA,i.freq,i.supportB,i.confidenceAtoB,i.confidenceBtoA,i.lift]
        t={"key"+str(first):assoc}
        son.append(t)
        first+=1
  
        
   
    
    assocresult={title:son}
    y = jsonify(assocresult)


    print(y) 
    print(type(y))

    print("TTTTTTTTTTTTTTTTTTTTTTTTTTt")
    return render_template("index.html",associations=associations)

@app.route("/search/<title>")
def deneme(title):
    title=title.replace("_", " ")
    try: 
        associations=assocs.query.filter(assocs.itemA==title)
    except:
        associations=[]
    son=[]
    first=1
    for i in associations:
        assoc=[i.itemA,i.itemB,i.freqA,i.supportA,i.freq,i.supportB,i.confidenceAtoB,i.confidenceBtoA,i.lift]
        t={"key"+str(first):assoc}
        son.append(t)
        first+=1
  
        
   
    
    assocresult={title:son}


    return jsonify(assocresult)
class assocs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    itemA=db.Column(db.String)
    itemB=db.Column(db.String)
    supportAB=db.Column(db.Float)
    freqA=db.Column(db.Integer)
    supportA=db.Column(db.Float)
    freq=db.Column(db.Integer)
    supportB=db.Column(db.Float)
    confidenceAtoB=db.Column(db.Float) 
    confidenceBtoA=db.Column(db.Float)
    lift=db.Column(db.Float)

    
if __name__=='__main__':
    app.run(debug=True)
