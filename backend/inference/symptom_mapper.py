def load_symptom_to_icd_mapping():
    """
    Load a predefined mapping of symptoms to ICD-10 codes.
    :return: A dictionary where keys are symptoms and values are ICD-10 codes.
    """
    # Mapping of symptoms to ICD-10 codes
    return {
        "fever": "R50",
        "cough": "R05",
        "shortness of breath": "R06.02",
        "chest pain": "R07.9",
        "headache": "R51",
        "nausea": "R11",
        "diarrhea": "A09",
        "fatigue": "R53",
        "sore throat": "J02.9",
        "rash": "R21",
    }

def map_symptom_to_icd(symptom):
    """
    Map a symptom to the corresponding ICD-10 code.
    :param symptom: The symptom to map.
    :return: ICD-10 code if a match is found, otherwise a message indicating no match.
    """
    symptom_mapping = load_symptom_to_icd_mapping()
    return symptom_mapping.get(symptom.lower(), "No matching ICD-10 code found for this symptom.")

if __name__ == "__main__":
    print("Enter the symptom to map to an ICD-10 code:")
    symptom = input().strip()
    icd_code = map_symptom_to_icd(symptom)
    print(f"ICD-10 Code: {icd_code}")