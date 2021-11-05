from flask import Flask, render_template, request
#import pickle
import joblib
import numpy as np
#model = pickle.load(open('loan_status.pkl', 'rb'))  # opening pickle file in read mode
model = joblib.load('data/loan_status.pkl')
app = Flask(__name__)  # initializing Flask app
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/',methods=["POST"])
def analyze():
    if request.method == 'POST':
        d1 = request.form['Gender']
        if (d1 == 'Male'):
            d1 = 1
        else:
            d1 = 0
        d2 = request.form['Married']
        if d2 == 'No':
            d2 = 0
        else:
            d2 = 1
        d3 = request.form['Dependents']
        if (d3 == '3+'):
            d3 = 3
        elif (d3=='2'):
            d3 = 2
        elif (d3=='1'):
            d3 = 1
        else:
            d3 = 0
        d4 = request.form['Education']
        if (d4 == 'Graduate'):
            d4 = 1
        else:
            d4 = 0
        d5 = request.form['Self_Employed']
        if (d5 == 'No'):
            d5 = 0
        else:
            d5 = 1
        d6 = request.form['ApplicantIncome']
        d7 = request.form['CoapplicantIncome']
        d8 = request.form['LoanAmount']
        d9 = request.form['Loan_Amount_Term']
        d10 = request.form['Credit_History']
        if (d10 == 'All debts paid'):
            d10 = 1.0
        else:
            d10= 0.0
        d11 = request.form['Property_Area']
        if (d11 == 'Urban'):
            d11 = 2
        elif (d11 == 'Rural'):
            d11 = 0
        else:
            d11 = 1
        #arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9,d10,d11]])
        
        sample_data =[d1, d2, d3, d4, d5, d6, d7, d8, d9,d10,d11]
        clean_data = [float(i) for i in sample_data]

		# Reshape the Data as a Sample not Individual Features
        ex1 = np.array(clean_data).reshape(1,-1)
        pred = model.predict(ex1)
        #print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        #print(pred)
        if pred == 0:
            return render_template('index.html', prediction_text="Sorry! You are not eligible for Loan.")
        else:
            return render_template('index.html', prediction_text="Congrats! You are eligible for Loan.")
        return render_template('index.html')
#app.run(host="0.0.0.0")            # deploy
#app.run(debug=True)                # run on local system
if __name__ == '__main__':
    app.run()
