#import libraries
import numpy as np
from flask import Flask, render_template,request
import pickle
#Initialize the flask App
app = Flask(__name__)
#model = pickle.load(open('C:\Users\Hsbc\Downloads\loan99\logistic_loan.pkl', 'rb'))
#pickle.dump(model, open('\Users\Hsbc\Downloads\logistic_loan.pkl', 'wb'))
import os
filepath = '/Users/hsbc/Downloads/loan99/logisticloan.pkl'
if os.path.exists(filepath):
    file = open('/Users/hsbc/Downloads/loan99/logisticloan.pkl', 'rb')
    codedata = pickle.load(file)
    file.close()
else:
    print("File not present at desired location")


#default page of our web-app
@app.route('/')
def home():
    return render_template('index99.html')
#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    print('inside predict')
    dependents = int(request.form['dependents']);
    education = int(request.form['education']);
    applicantIncome = float(request.form['Applicant_Income'])
    loan_amount = float(request.form['Loan_amount'])
    #loan_term = int(request.form['Loan_term'])
    credit_history = int(request.form['Credit_history'])
    propertyArea = int(request.form['property_area'])
    result = ValuePredictor([dependents,education,applicantIncome,loan_amount,credit_history,propertyArea])
    print(result)
    if result == 0 :
        return "Sorry You are not eligible to avail loan"
    else:
        return "Congrats , You are eligible for avail the loan"
        
    #For rendering results on HTML GUI
   # int_features = [float(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)
    #output = round(prediction[0], 2) 
    #return render_template('index99.html', prediction_text='loan statusis :{}'.format(output))
    return "Hello World !"

#def isEligibleForLoan():
 #   with open('logistic_loan.pkl','rb') as f:
  #      model = pickle.load(f);
        
# prediction function
def ValuePredictor(to_predict_list):
    print(to_predict_list)
    to_predict = np.array(to_predict_list).reshape(1, 6)
    loaded_model = pickle.load(open("logisticloan.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]



@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)