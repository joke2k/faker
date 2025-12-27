from .. import BaseProvider, ElementsType


class Provider(BaseProvider):
    """Provider for generating healthcare/medical-related fake data."""

    diseases: ElementsType[str] = (
        "Type 2 Diabetes",
        "Essential Hypertension",
        "Hyperlipidemia",
        "Coronary Artery Disease",
        "Chronic Obstructive Pulmonary Disease",
        "Asthma",
        "Chronic Kidney Disease",
        "Osteoarthritis",
        "Rheumatoid Arthritis",
        "Depression",
        "Anxiety Disorder",
        "Gastroesophageal Reflux Disease",
        "Obesity",
        "Hypothyroidism",
        "Atrial Fibrillation",
        "Congestive Heart Failure",
        "Pneumonia",
        "Urinary Tract Infection",
        "Acute Bronchitis",
        "Anemia",
        "Migraine",
        "Stroke",
        "Alzheimer's Disease",
        "Breast Cancer",
        "Prostate Cancer",
        "Lung Cancer",
        "COVID-19",
        "Influenza",
        "Osteoporosis",
        "Peripheral Artery Disease",
    )

    icd10_codes: ElementsType[str] = (
        "E11.9",
        "I10",
        "E78.5",
        "I25.10",
        "J44.9",
        "J45.909",
        "N18.9",
        "M17.9",
        "M79.1",
        "F32.9",
        "F41.9",
        "K21.9",
        "E66.9",
        "E03.9",
        "I48.91",
        "I50.9",
        "J18.9",
        "N39.0",
        "J20.9",
        "D64.9",
        "G43.909",
        "I63.9",
        "G30.9",
        "R10.9",
        "R50.9",
        "R06.00",
        "R53.81",
        "Z00.00",
        "Z79.899",
        "Z68.1",
        "C50.919",
        "C61",
        "C34.90",
        "U07.1",
        "J11.1",
        "M81.0",
        "I73.9",
        "K70.30",
        "G20",
        "E10.9",
    )

    medical_specialties: ElementsType[str] = (
        "Cardiology",
        "Dermatology",
        "Endocrinology",
        "Gastroenterology",
        "Hematology",
        "Infectious Disease",
        "Nephrology",
        "Neurology",
        "Oncology",
        "Pulmonology",
        "Rheumatology",
        "Allergy and Immunology",
        "Family Medicine",
        "Internal Medicine",
        "Pediatrics",
        "Psychiatry",
        "Obstetrics and Gynecology",
        "Orthopedics",
        "Urology",
        "Ophthalmology",
        "Otolaryngology",
        "Anesthesiology",
        "Radiology",
        "Pathology",
        "Emergency Medicine",
        "General Surgery",
        "Plastic Surgery",
        "Neurosurgery",
        "Physical Medicine and Rehabilitation",
    )

    hospital_departments: ElementsType[str] = (
        "Emergency Department",
        "Intensive Care Unit (ICU)",
        "Cardiac Care Unit (CCU)",
        "Operating Room",
        "Labor and Delivery",
        "Pediatrics",
        "Maternity Ward",
        "Oncology",
        "Radiology",
        "Laboratory",
        "Pharmacy",
        "Physical Therapy",
        "Occupational Therapy",
        "Respiratory Therapy",
        "Surgery",
        "Inpatient Ward",
        "Outpatient Clinic",
        "Psychiatric Ward",
        "Rehabilitation Unit",
        "Endoscopy Suite",
    )

    generic_drugs: ElementsType[str] = (
        "Atorvastatin",
        "Levothyroxine",
        "Lisinopril",
        "Metformin",
        "Amlodipine",
        "Metoprolol",
        "Omeprazole",
        "Simvastatin",
        "Losartan",
        "Gabapentin",
        "Hydrochlorothiazide",
        "Sertraline",
        "Amoxicillin",
        "Albuterol",
        "Citalopram",
        "Pantoprazole",
        "Trazodone",
        "Fluoxetine",
        "Tramadol",
        "Clopidogrel",
    )

    brand_drugs: ElementsType[str] = (
        "Lipitor",
        "Synthroid",
        "Prinivil",
        "Glucophage",
        "Norvasc",
        "Lopressor",
        "Prilosec",
        "Zocor",
        "Cozaar",
        "Neurontin",
        "Zoloft",
        "Prozac",
        "Effexor",
        "Lexapro",
        "Cymbalta",
        "Plavix",
        "Eliquis",
        "Ozempic",
        "Jardiance",
        "Farxiga",
    )

    symptoms: ElementsType[str] = (
        "Fever",
        "Cough",
        "Shortness of Breath",
        "Headache",
        "Fatigue",
        "Abdominal Pain",
        "Nausea",
        "Vomiting",
        "Diarrhea",
        "Chest Pain",
        "Dizziness",
        "Rash",
        "Sore Throat",
        "Joint Pain",
        "Back Pain",
        "Coughing Blood",
        "Weight Loss",
        "Swelling",
        "Blurred Vision",
        "Palpitations",
    )

    blood_types: ElementsType[str] = (
        "A+",
        "A-",
        "B+",
        "B-",
        "AB+",
        "AB-",
        "O+",
        "O-",
    )

    allergies: ElementsType[str] = (
        "Penicillin",
        "Peanuts",
        "Tree Nuts",
        "Shellfish",
        "Fish",
        "Milk",
        "Eggs",
        "Soy",
        "Wheat",
        "Sesame",
        "Latex",
        "Bee Sting",
        "Pollen",
        "Dust Mites",
        "Pet Dander",
        "Sulfa Drugs",
        "Aspirin",
        "Ibuprofen",
    )

    medical_procedures: ElementsType[str] = (
        "Blood Test",
        "MRI Scan",
        "CT Scan",
        "X-Ray",
        "Ultrasound",
        "Colonoscopy",
        "Endoscopy",
        "Appendectomy",
        "Cholecystectomy",
        "C-Section",
        "Hysterectomy",
        "Knee Replacement",
        "Hip Replacement",
        "Cataract Surgery",
        "Biopsy",
        "Physical Therapy Session",
        "Electrocardiogram (ECG)",
        "Echocardiogram",
        "Vaccination",
        "Wound Debridement",
    )

    insurance_plans: ElementsType[str] = (
        "PPO",
        "HMO",
        "EPO",
        "POS",
        "Medicare",
        "Medicaid",
        "High-Deductible Health Plan (HDHP)",
        "Private Insurance",
        "Employer-Sponsored",
        "Medicare Advantage",
        "TRICARE",
        "Veterans Affairs (VA)",
    )

    vital_signs: ElementsType[str] = (
        "Blood Pressure",
        "Heart Rate",
        "Respiratory Rate",
        "Body Temperature",
        "Oxygen Saturation",
        "Body Mass Index (BMI)",
        "Blood Glucose",
        "Pain Level",
    )

    def disease(self) -> str:
        return self.random_element(self.diseases)

    def icd10_code(self) -> str:
        return self.random_element(self.icd10_codes)

    def medical_specialty(self) -> str:
        return self.random_element(self.medical_specialties)

    def hospital_department(self) -> str:
        return self.random_element(self.hospital_departments)

    def generic_drug(self) -> str:
        return self.random_element(self.generic_drugs)

    def brand_drug(self) -> str:
        return self.random_element(self.brand_drugs)

    def symptom(self) -> str:
        return self.random_element(self.symptoms)

    def blood_type(self) -> str:
        return self.random_element(self.blood_types)

    def allergy(self) -> str:
        return self.random_element(self.allergies)

    def medical_procedure(self) -> str:
        return self.random_element(self.medical_procedures)

    def insurance_plan(self) -> str:
        return self.random_element(self.insurance_plans)

    def vital_sign(self) -> str:
        return self.random_element(self.vital_signs)

    def diagnosis(self) -> str:
        return f"{self.disease()} ({self.icd10_code()})"
