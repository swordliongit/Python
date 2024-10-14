import re


def extract_year(text):
    text = text.strip()  # Remove any leading/trailing spaces
    match = re.search(r'(?:-\s*|\(\s*)\b(\d{4})\b\s*\)?', text)
    if match:
        return match.group(1)
    return None


# Examples
print(extract_year("Die Drei - 2023"))  # Output: 2023
print(extract_year("Die Drei ( 2023 )"))  # Output: 2023
print(extract_year("Die Drei-2023"))  # Output: 2023
print(extract_year("Die Drei(2023)"))  # Output: 2023
print(extract_year("Die Drei (2023)"))  # Output: 2023
print(extract_year("Die Drei (2023 )"))  # Output: 2023
print(extract_year("Die Drei - 202"))  # Output: None
print(extract_year("Die Drei ( 202 )"))  # Output: None
