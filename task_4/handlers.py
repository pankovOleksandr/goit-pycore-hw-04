import re

contacts = {}

def say_greeting():
    print("How can I help you?")        

def add_contact(name: str, phone: str) -> None:
    contacts[name] = normalize_phone(phone)

def change_contact(name: str, phone: str) -> None:
    if name not in contacts:
        raise ValueError("Contact is not found")

    contacts[name] = normalize_phone(phone)

def show_phone(name: str) -> str:
    if name not in contacts:
        raise ValueError("Contact is not exist")

    return contacts[name]

def show_all() -> dict:
    return contacts


def normalize_phone(phone_number: str) -> str:
    country_code = "38"
    pattern = r"[+\d]"
    phone_number = "".join(re.findall(pattern, phone_number))

    if not phone_number.startswith("+"):
        phone_number = re.sub(fr"^({country_code})?", f"+{country_code}", phone_number)

    if len(phone_number) != 13:
        raise ValueError(f"Invalid phone number: {phone_number}")

    return phone_number