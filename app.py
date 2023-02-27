# This contains the code as well as the index for the api

# 1. Importing Necessary modules
import pickle

import uvicorn
from fastapi import FastAPI

from patientinfohdfe import patientData

# 2. Declaring our FastAPI instance/ Create the app object
app = FastAPI()
pickle_in = open("mlmodel.pkl", "rb")
classifier = pickle.load(pickle_in)


# 3. Defining path operation for root endpoint. Opens at http://127.0.0.1:8000/
@app.get('/')
def main():
    return {'message': 'Welcome to our Project!'}


# 4. Defining path operation for /name endpoint. Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def hello_name(name: str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to our Project!, {name}'}


# 5. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted diagnosis with the confidence
@app.post('/predict')
def predict_disease(data: patientData):
    data = data.dict()  # 11 inputs
    Age = data['Age']
    Sex = data['Sex']
    ChestPain = data['ChestPain']
    RestingBP = data['RestingBP']
    Cholestral = data['Cholestral']
    FastingBS = data['FastingBS']
    RestingECG = data['RestingECG']
    MaxHR = data['MaxHR']
    Exercising = data['Exercising']
    Oldpeak = data['Oldpeak']
    ST_Slope = data['ST_Slope']

    # print(random_forest_model.predict([[inputs...]]))
    # the model takes the inputs passed through the api
    prediction: object = classifier.predict([[Age, Sex,ChestPain, RestingBP, Cholestral, FastingBS, RestingECG, MaxHR, Exercising, Oldpeak, ST_Slope]])

    # If prediction = 0 then patient is Demented and if prediction = 1, patient is Nondemented
    if prediction[0] > 0.5:
        prediction = "Heart Disease"
    else:
        prediction = "No Heart Disease"
    return {
        'prediction': prediction
    }


# 6. Run the API with uvicorn. Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# To run the API, first change the directory to the current project then use the command,
# uvicorn app:app --reload
# Then use swagger through http://127.0.0.1:8000/docs
