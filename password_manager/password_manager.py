# password are encrypted
from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter your master password")

key = load_key() + master_pwd.encode()
fer = Fernet(key)


# key + password + text to encrypt = random text
# random text + key + password = text to encrypt



def view():
    with open("password.txt","r") as f:
        for line in f:
            user, passd = line.rstrip().split("|")
            print("User :"+user, ", Password :"+  fer.decrypt(passd.encode()).decode())


def add():
    name = input("Name : ")
    pwd = input("password : ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode()+ "\n")


while True:
    mode = input("Would you like to view password or add passwords (view/ add) and q to quit ").lower()

    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode.")
        continue