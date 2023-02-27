# File to create a structure for the input to the ML model
# This way the attributes of the class patientData can be used as features of the data.

from pydantic import BaseModel


# Class which describes patient data measurements
# Contains 11 attibutes/inputs
class patientData(BaseModel):
    Age: int
    Sex: int
    ChestPain:int
    RestingBP: int
    Cholestral: int
    FastingBS: int
    RestingECG: int
    MaxHR: int
    Exercising: int
    Oldpeak: float
    ST_Slope: int