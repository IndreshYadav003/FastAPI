# Step 1 pip install pydantic
# Step 2 pip show pydantic
# step 3 run
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


def insert_patients_data(patient: Patient):
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("Inserted data successfully.")


patients_info = {
    "name": "Indresh",
    "age": 37
}

patient1 = Patient(**patients_info)

insert_patients_data(patient1)