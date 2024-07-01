from flask import Flask, render_template, request
import utils
from utils import preprocessdata

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Fetch form data
        customer_age = request.form.get('customer_age')
        employment_duration = request.form.get('employment_duration')
        loan_int_rate = request.form.get('loan_int_rate')
        term_years = request.form.get('term_years')
        historical_default = request.form.get('historical_default')
        cred_hist_length = request.form.get('cred_hist_length')
        customer_income_log = request.form.get('customer_income_log')
        loan_amnt_log = request.form.get('loan_amnt_log')
        home_ownership_MORTGAGE = request.form.get('home_ownership_MORTGAGE')
        home_ownership_OTHER = request.form.get('home_ownership_OTHER')
        home_ownership_OWN = request.form.get('home_ownership_OWN')
        home_ownership_RENT = request.form.get('home_ownership_RENT')
        loan_intent_DEBTCONSOLIDATION = request.form.get('loan_intent_DEBTCONSOLIDATION')
        loan_intent_EDUCATION = request.form.get('loan_intent_EDUCATION')
        loan_intent_HOMEIMPROVEMENT = request.form.get('loan_intent_HOMEIMPROVEMENT')
        loan_intent_MEDICAL = request.form.get('loan_intent_MEDICAL')
        loan_intent_PERSONAL = request.form.get('loan_intent_PERSONAL')
        loan_intent_VENTURE = request.form.get('loan_intent_VENTURE')
        loan_grade_A = request.form.get('loan_grade_A')
        loan_grade_B = request.form.get('loan_grade_B')
        loan_grade_C = request.form.get('loan_grade_C')
        loan_grade_D = request.form.get('loan_grade_D')
        loan_grade_E = request.form.get('loan_grade_E')
        loan_grade_F = request.form.get('loan_grade_F')
        
        prediction = preprocessdata(
            customer_age, employment_duration, loan_int_rate, term_years,
            historical_default, cred_hist_length, customer_income_log, loan_amnt_log,
            home_ownership_MORTGAGE,home_ownership_OTHER,home_ownership_OWN,home_ownership_RENT,loan_intent_DEBTCONSOLIDATION,loan_intent_EDUCATION, loan_intent_HOMEIMPROVEMENT,
            loan_intent_MEDICAL, loan_intent_PERSONAL, loan_intent_VENTURE, loan_grade_A,
            loan_grade_B, loan_grade_C, loan_grade_D, loan_grade_E , loan_grade_F
        )

        return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.debug = True
    app.run()