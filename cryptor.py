#!/usr/bin/env python

def encrypt_decrypt(input_string, secret_number):
    result = ""
    for x in input_string:
        result += chr(ord(x) ^ int(secret_number))
    return result

# Vraag de gebruiker om een geheime sleutel in te voeren
my_secret_key = input("Voer je geheime code in: ")

# Vraag de gebruiker om te kiezen of ze willen encrypten of decrypten
choice = input("Wil je een text encrypten of decrypten? (e/d): ").strip().lower()

if choice == "e":
    # Vraag de gebruiker om de tekst die moet worden versleuteld
    original_text = input("Vul de text in die je wil versleutelen: ")
    encrypted_text = encrypt_decrypt(original_text, my_secret_key)
    print(f"Versleutelde text: {encrypted_text}")

elif choice == "d":
    # Vraag de gebruiker om de te ontcijferen tekst in te voeren
    encrypted_text = input("Vul de text in die je wil ontsleutelen: ")
    decrypted_text = encrypt_decrypt(encrypted_text, my_secret_key)
    print(f"Ontsleutelde text: {decrypted_text}")
