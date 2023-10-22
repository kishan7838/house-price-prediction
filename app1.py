from turtle import home
from flask import Flask,request, render_template
from joblib import load
import numpy as np
import os

img_f = os.path.join('static', 'img')

app = Flask(__name__,template_folder="Website")
app.config['UPLOAD_FOLDER'] = img_f

model = load('realestate.joblib')

@app.route('/')
@app.route('/home.html')
def hello():
    home = os.path.join(app.config['UPLOAD_FOLDER'], 'hero.png')
    return render_template("home.html", h = home)


@app.route('/about.html')
def hello_about():
    about = os.path.join(app.config['UPLOAD_FOLDER'], 'about.png')
    team1 = os.path.join(app.config['UPLOAD_FOLDER'], 'team-1.jpg')
    team2 = os.path.join(app.config['UPLOAD_FOLDER'], 'team-2.jpg')
    team3 = os.path.join(app.config['UPLOAD_FOLDER'], 'team-3.jpg')
    
    return render_template("about.html", ab =about,t1 = team1, t2 = team2, t3 = team3)


@app.route('/price.html')
def hello_price():
    return render_template("price.html")

@app.route('/contact.html')
def hello_contact():
    return render_template("contact.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    data1= request.form['a']
    data2= request.form['b']
    data3= request.form['c']
    data4= request.form['d']
    data5= request.form['e']
    data6= request.form['f']
    data7= request.form['g']
    data8= request.form['h']
    data9= request.form['i']
    data10= request.form['j']
    data11= request.form['k']
    data12= request.form['l']
    data13= request.form['m']
    arr=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13]])
    pred=model.predict(arr)
    output = round(pred[0],2)
    return render_template('price.html', data=f"price of the property according to the features you entered is ₹{output} Lakhs.")


if __name__ == '__main__':
    app.run(debug=True)