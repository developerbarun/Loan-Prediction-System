import numpy as np
import joblib
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def preprocessdata(customer_age, employment_duration, loan_int_rate, term_years,
                   historical_default, cred_hist_length, customer_income_log, loan_amnt_log,
                   home_ownership_MORTGAGE,home_ownership_OTHER,home_ownership_OWN,home_ownership_RENT,loan_intent_DEBTCONSOLIDATION,loan_intent_EDUCATION, loan_intent_HOMEIMPROVEMENT,
                   loan_intent_MEDICAL, loan_intent_PERSONAL, loan_intent_VENTURE, loan_grade_A,
                   loan_grade_B, loan_grade_C, loan_grade_D, loan_grade_E,loan_grade_F):

    try:
        # Log input data
        logging.info(f"Received input data: {locals()}")

        # Ensure all inputs are converted to the appropriate numeric type
        test_data = np.array([[
            int(customer_age), float(employment_duration), float(loan_int_rate), float(term_years),
            float(historical_default), float(cred_hist_length), float(customer_income_log), float(loan_amnt_log),
            float(home_ownership_MORTGAGE), bool(home_ownership_OTHER),int(home_ownership_OWN),float(home_ownership_RENT),int(loan_intent_DEBTCONSOLIDATION), float(loan_intent_EDUCATION), float(loan_intent_HOMEIMPROVEMENT),
            float(loan_intent_MEDICAL), float(loan_intent_PERSONAL), float(loan_intent_VENTURE), float(loan_grade_A),
            float(loan_grade_B), float(loan_grade_C), float(loan_grade_D), float(loan_grade_E) , float(loan_grade_F)
        ]])

        logging.info(f"Formatted test data: {test_data}")

        # Load the model
        trained_model = joblib.load("model.pkl")
        logging.info("Model loaded successfully")

        # Make prediction
        prediction = trained_model.predict(test_data)
        logging.info(f"Model prediction: {prediction}")
        return prediction[0]
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return "Error"











# import numpy as np
# import joblib

# def preprocessdata(customer_age, employment_duration, loan_int_rate, term_years,
#                    historical_default, cred_hist_length, customer_income_log, loan_amnt_log,
#                    home_ownership_MORTGAGE,home_ownership_OTHER,home_ownership_OWN,home_ownership_RENT,loan_intent_DEBTCONSOLIDATION,loan_intent_EDUCATION, loan_intent_HOMEIMPROVEMENT,
#                    loan_intent_MEDICAL, loan_intent_PERSONAL, loan_intent_VENTURE, loan_grade_A,
#                    loan_grade_B, loan_grade_C, loan_grade_D, loan_grade_E):


#     test_data = np.array([[
#             float(customer_age), float(employment_duration), float(loan_int_rate), float(term_years),
#             float(historical_default), float(cred_hist_length), float(customer_income_log), float(loan_amnt_log),
#             float(home_ownership_MORTGAGE), bool(home_ownership_OTHER),int(home_ownership_OWN),float(home_ownership_RENT),int(loan_intent_DEBTCONSOLIDATION), float(loan_intent_EDUCATION), float(loan_intent_HOMEIMPROVEMENT),
#             float(loan_intent_MEDICAL), float(loan_intent_PERSONAL), float(loan_intent_VENTURE), float(loan_grade_A),
#             float(loan_grade_B), float(loan_grade_C), float(loan_grade_D), float(loan_grade_E)
#         ]])

#     trained_model = joblib.load("model.pkl")

#     prediction = trained_model.predict(test_data)

#     return prediction


# import numpy as np
# import joblib
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO)

# def preprocessdata(customer_age, employment_duration, loan_int_rate, term_years,
#                    historical_default, cred_hist_length, customer_income_log, loan_amnt_log,
#                    home_ownership_MORTGAGE,home_ownership_OTHER,home_ownership_OWN,home_ownership_RENT,loan_intent_DEBTCONSOLIDATION,loan_intent_EDUCATION, loan_intent_HOMEIMPROVEMENT,
#                    loan_intent_MEDICAL, loan_intent_PERSONAL, loan_intent_VENTURE, loan_grade_A,
#                    loan_grade_B, loan_grade_C, loan_grade_D, loan_grade_E):

#     try:
#         # Log input data
#         logging.info(f"Received input data: {locals()}")

#         # Ensure all inputs are converted to the appropriate numeric type
#         test_data = np.array([[
#             float(customer_age), float(employment_duration), float(loan_int_rate), float(term_years),
#             float(historical_default), float(cred_hist_length), float(customer_income_log), float(loan_amnt_log),
#             float(home_ownership_MORTGAGE), bool(home_ownership_OTHER),int(home_ownership_OWN),float(home_ownership_RENT),int(loan_intent_DEBTCONSOLIDATION), float(loan_intent_EDUCATION), float(loan_intent_HOMEIMPROVEMENT),
#             float(loan_intent_MEDICAL), float(loan_intent_PERSONAL), float(loan_intent_VENTURE), float(loan_grade_A),
#             float(loan_grade_B), float(loan_grade_C), float(loan_grade_D), float(loan_grade_E)
#         ]])

#         logging.info(f"Formatted test data: {test_data}")

#         # Load the model
#         trained_model = joblib.load("model.pkl")
#         logging.info("Model loaded successfully")

#         # Make prediction
#         prediction = trained_model.predict(test_data)
#         logging.info(f"Model prediction: {prediction}")
#         print(prediction[0])
#         return prediction[0]
#     except Exception as e:
#         logging.error(f"Error during prediction: {e}")
#         return "Error aa gaya"
