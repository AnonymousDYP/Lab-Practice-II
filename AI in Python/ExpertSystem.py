# Define the knowledge base as a dictionary with symptom-disease mappings
knowledge_base = {
    ('Fever', 'Cough', 'Shortness of breath'): 'COVID-19',
    ('Fever', 'Cough', 'Fatigue'): 'Influenza',
    ('Fever', 'Chest pain', 'Shortness of breath'): 'Pneumonia',
    ('Chest pain', 'Shortness of breath', 'Nausea'): 'Heart attack',
    ('Headache', 'Sore throat', 'Fever'): 'Flu',
    ('Headache', 'Nausea', 'Vomiting'): 'Migraine',
    ('Abdominal pain', 'Nausea', 'Vomiting'): 'Gastroenteritis',
    ('Abdominal pain', 'Diarrhea', 'Fever'): 'Salmonella',
    ('Rash', 'Fever', 'Joint pain'): 'Zika virus',
    ('Rash', 'Fever', 'Joint pain'): 'Chikungunya virus',
    ('Rash', 'Fever', 'Fatigue'): 'Measles',
    ('Rash', 'Fever', 'Headache'): 'Rubella',
    ('Chest pain', 'Shortness of breath', 'Swelling'): 'Pulmonary embolism',
    ('Seizures', 'Memory loss', 'Headache'): 'Epilepsy',
    ('Muscle weakness', 'Numbness', 'Tingling'): 'Multiple sclerosis'
}

# Define a function to diagnose diseases based on symptoms
def diagnose(*symptoms):
    # print(symptoms)
    for symptom_set, disease in knowledge_base.items():
        if set(symptoms) == set(symptom_set):
            return disease
    return "Unknown disease"

# Get symptoms input from user
symptoms = []
print("-------------------- Medical Diagnosis Expert System --------------------")

ch=input("Would you like to answer some of the question related to yuor health? : ")
if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
    ch=input("Do you have Fever? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append('Fever')
    ch=input("Do you have Cough? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Cough")

    ch=input("Do you have Chest Pain? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Chest Pain")

    ch=input("Do you have Rash? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Rash")

    ch=input("Do you have Headache? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Headache")

    ch=input("Do you have Muscle Weakness? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Muscle Weakness")

    ch=input("Do you have Abdominal pain? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Abdominal pain")

    ch=input("Do you have Seizures? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Seizures")
    ch=input("Do you have Shortness of breath? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Shortness of breath")

    ch=input("Do you have Fatigue? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Fatigue")

    ch=input("Do you have Nausea? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Nausea")

    ch=input("Do you have Vomiting? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Vomiting")

    ch=input("Do you have Diarrhea? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Diarrhea")

    ch=input("Do you have Joint pain? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Joint pain")

    ch=input("Do you have Memory loss? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Memory loss")

    ch=input("Do you have Numbness? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Numbness")

    ch=input("Do you have Tingling? : ")
    if(ch=="YES" or ch=="yes" or ch=="y" or ch=="Y"):
        symptoms.append("Tingling")

# Diagnose the disease based on the symptoms entered by the user
print(symptoms)
disease = diagnose(*symptoms)
print("Based on your symptoms, you might have", disease)