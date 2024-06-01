from flask import Flask, json, jsonify, Response, request, render_template
from model import engine, User
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS

app=Flask(__name__)
CORS(app)



@app.route('/enter', methods=['POST'])
def n():
    paylod=request.json
    Session=sessionmaker(engine)
    session=Session()
    ne=User(name=paylod['name'], Class=paylod['class'])
    session.add(ne)
    session.commit()
    return jsonify(message="data inserted"),201


@app.route('/info', methods=['GET'])
def get_data():
    Session=sessionmaker(engine)
    session=Session()
    n = session.query(User).all()
    h=[]
    for i  in n:
        h.append({"name":i.name, "class":i.Class})
        
    return jsonify(message="success full data ge", data=h), 200


@app.route('/')
def home():
    return render_template('ex.html')



        
    
    
   




