import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('model.sav','rb'))


def covid_prediction(input_data):
    # changing the input data to numpy array
    input_data_array = np.array(input_data)

    prediction = loaded_model.predict(input_data_array)
    print(prediction)

    if(prediction[0][0] >= 0.70):
        disp_msg = f"There is {round(prediction[0][0] * 100)}% chance that you have covid. You must consult a doctor as soon as possible."
    elif(prediction[0][0] > 0.40 and prediction[0][0] < 0.70):
        disp_msg = f"There is {round(prediction[0][0] * 100)}% chance that you have covid. We recommend you consult a doctor."

    else:
        disp_msg = f"There is only {round(prediction[0][0] * 100)}% chance that you have covid. You are less likely to be infected by covid, but you may stil get tested."
    return disp_msg


def main():
    # giving a title
    st.title('Covid prediction web app')

    # getting the input data from the user

    st.title('(yes/no)')
    Breathing_Problem1 = st.text_input("Breathing Problem: ")
    if(Breathing_Problem1 == 'yes'):
        Breathing_Problem=1
    else:
        Breathing_Problem = 0
    Fever1 = st.text_input("Fever: ")
    if(Fever1 == 'yes'):
        Fever=1
    else:
        Fever = 0
    Dry2 = st.text_input("Dry: ")
    if(Dry2 == 'yes'):
        Dry=1
    else:
        Dry = 0
    Cough1 = st.text_input("Cough: ")
    if(Cough1 == 'yes'):
        Cough=1
    else:
        Cough = 0
    Sore_throat1 = st.text_input("Sore Throat: ")
    if(Sore_throat1 == 'yes'):
        Sore_throat=1
    else:
        Sore_throat = 0
    Running_Nose1 = st.text_input("Running_Nose: ")
    if(Running_Nose1 == 'yes'):
        Running_Nose=1
    else:
        Running_Nose = 0
    Asthma1 = st.text_input("Asthma: ")
    if(Asthma1 == 'yes'):
        Asthma=1
    else:
        Asthma = 0
    Chronic_Lung_Disease1 = st.text_input("Chronic Lung Disease: ")
    if(Chronic_Lung_Disease1 == 'yes'):
        Chronic_Lung_Disease=1
    else:
        Chronic_Lung_Disease = 0
    Headache1 = st.text_input("Headache: ")
    if(Headache1 == 'yes'):
        Headache=1
    else:
        Headache = 0
    Heart_Disease1 = st.text_input("Heart_Disease: ")
    if(Heart_Disease1 == 'yes'):
        Heart_Disease = 1
    else:
        Heart_Disease = 0
    Diabetes1 = st.text_input("Diabetes: ")
    if(Diabetes1 == 'yes'):
        Diabetes=1
    else:
        Diabetes = 0
    Hyper_Tension1 = st.text_input("Hyper_Tension: ")
    if(Hyper_Tension1 == 'yes'):
        Hyper_Tension=1
    else:
        Hyper_Tension = 0
    Fatigue1 = st.text_input("Fatigue: ")
    if(Fatigue1 == 'yes'):
        Fatigue=1
    else:
        Fatigue = 0
    Gastrointestinal1 = st.text_input("Gastrointestinal: ")
    if(Gastrointestinal1 == 'yes'):
        Gastrointestinal=1
    else:
        Gastrointestinal = 0
    Abroad_Travel1 = st.text_input("Abroad Travel: ")
    if(Abroad_Travel1 == 'yes'):
        Abroad_Travel=1
    else:
        Abroad_Travel = 0
    Contact_with_COVID_Patient1 = st.text_input("Contact with COVID patient: ")
    if(Contact_with_COVID_Patient1 == 'yes'):
        Contact_with_COVID_Patient=1
    else:
        Contact_with_COVID_Patient = 0
    Attended_Large_Gathering1 = st.text_input("Attended Large Gathering: ")
    if(Attended_Large_Gathering1 == 'yes'):
        Attended_Large_Gathering=1
    else:
        Attended_Large_Gathering = 0
    Visited_Public_Exposed_Places1 = st.text_input("Visited Public Exposed Places: ")
    if(Visited_Public_Exposed_Places1 == 'yes'):
        Visited_Public_Exposed_Places=1
    else:
        Visited_Public_Exposed_Places = 0
    Fwipep1 = st.text_input("Family Working In Public Exposed Places: ")
    if(Fwipep1 == 'yes'):
        Fwipep=1
    else:
        Fwipep = 0
    Wearing_Masks1 = st.text_input("Wearing masks: ")
    if(Wearing_Masks1 == 'yes'):
        Wearing_Masks=1
    else:
        Wearing_Masks = 0

    # code for Prediction
    diagnosis = ''

    # creating a button for prediction

    if st.button('COVID test result: '):
        diagnosis = covid_prediction([[Breathing_Problem, Fever, Dry, Cough, Sore_throat, Running_Nose, Asthma,Chronic_Lung_Disease, Headache, Heart_Disease, Diabetes, Hyper_Tension, Fatigue,Gastrointestinal, Abroad_Travel, Contact_with_COVID_Patient,Attended_Large_Gathering, Visited_Public_Exposed_Places, Fwipep, Wearing_Masks]])

    st.success(diagnosis)





if __name__ == '__main__':
    main()

