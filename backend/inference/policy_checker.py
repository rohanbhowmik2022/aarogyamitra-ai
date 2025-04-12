def load_policy_mapping():
    """
    Load a predefined mapping of ICD-10 codes to insurance policies.
    :return: A dictionary where keys are ICD-10 codes and values are policy details.
    """
    # Mapping of ICD-10 codes to policies
    return {
        "A00": "Policy A: Covers cholera treatment",
        "B20": "Policy B: Covers HIV-related conditions",
        "C34": "Policy C: Covers lung cancer treatment",
        "E11": "Policy D: Covers Type 2 diabetes treatment",
        "I10": "Policy E: Covers essential hypertension treatment",
    }

def match_icd_to_policy(icd_code):
    """
    Match an ICD-10 code to the corresponding insurance policy.
    :param icd_code: The ICD-10 code to match.
    :return: Policy details if a match is found, otherwise a message indicating no match.
    """
    policy_mapping = load_policy_mapping()
    return policy_mapping.get(icd_code, "No matching policy found for this ICD-10 code.")

if __name__ == "__main__":
    icd_code = input("Enter the ICD-10 code: ").strip().upper()
    policy_details = match_icd_to_policy(icd_code)
    print(policy_details)