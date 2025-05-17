from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64
import os

def create_keys():
    secret_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    open_key = secret_key.public_key()
    
    with open("secret.pem", "wb") as key_file:
        key_file.write(secret_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    with open("public.pem", "wb") as key_file:
        key_file.write(open_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print(">> New keys created successfully.")

def get_keys():
    try:
        with open("secret.pem", "rb") as key_file:
            secret = serialization.load_pem_private_key(
                key_file.read(),
                password=None
            )
        
        with open("public.pem", "rb") as key_file:
            open_key = serialization.load_pem_public_key(
                key_file.read()
            )
        
        return secret, open_key
    except FileNotFoundError:
        print("No keys found. Create keys first.")
        return None, None

def lock_message(text, open_key):
    locked = open_key.encrypt(
        text.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(locked).decode()

def unlock_message(locked_text, secret):
    locked_bytes = base64.b64decode(locked_text.encode())
    unlocked = secret.decrypt(
        locked_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return unlocked.decode()

def clear_display():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_program():
    while True:
        clear_display()
        print("=== SECURE MESSAGING TOOL ===")
        print("1. Make new keys")
        print("2. Lock message")
        print("3. Unlock message")
        print("4. Quit")
        print("="*30)
        
        selection = input("Your choice (1-4): ").strip()

        if selection == "1":
            clear_display()
            print("=== CREATE NEW KEYS ===")
            create_keys()
            input("\nPress Enter to continue...")
            
        elif selection == "2":
            clear_display()
            print("=== LOCK MESSAGE ===")
            secret, open_key = get_keys()
            if open_key:
                text = input("Message to lock: ")
                locked = lock_message(text, open_key)
                print("\nLocked message:")
                print("-"*30)
                print(locked)
                print("-"*30)
            input("\nPress Enter to continue...")
            
        elif selection == "3":
            clear_display()
            print("=== UNLOCK MESSAGE ===")
            secret, open_key = get_keys()
            if secret:
                locked = input("Locked message: ")
                try:
                    unlocked = unlock_message(locked, secret)
                    print("\nOriginal message:")
                    print("-"*30)
                    print(unlocked)
                    print("-"*30)
                except Exception as error:
                    print(f"\nFailed: {str(error)}")
            input("\nPress Enter to continue...")
            
        elif selection == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid option. Try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    run_program()