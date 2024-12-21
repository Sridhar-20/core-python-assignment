class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def to_dict(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Disease": self.disease
        }

def search_patients_by_disease(patients, disease):
    matching_patients = []
    for patient in patients:
        if patient["Disease"].lower() == disease.lower():
            matching_patients.append(patient["Name"])
    return matching_patients

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"

matching_patients = search_patients_by_disease(patients, search_disease)

print(f"Patients with {search_disease}: {matching_patients}")

