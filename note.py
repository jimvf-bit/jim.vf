import os
from datetime import datetime

def clear_screen():
    os.system("clear")

def register():
    print("\n\t\t\t\t\t <<<REGISTRATSIYA>>>")
    username = input("Nick name: ")
    last_name = input("Last name: ")
    user_name = input("User name: ")
    password = input("Parolni kiriting: ")
    return user_name, password

def add_note(username):
    print(f"Salom {username}")
    now = datetime.now()
    note = input(f"Zametkangizni kiriting:\nKiritilgan sana {now}\n>>>")
    return note, now

def login():
    print("\n\t\t\t\t\t <<<LOGIN>>>")
    user_name = input("User name: ")
    password = input("Parolni kiriting: ")
    return user_name, password

def main():
    a = []
    za = []
    vaqt = []
    while True:
        clear_screen()
        print("\n\t\t\t\t\t <<<REGISTRATSIYA>>>")
        choice = input("Siz ro'yxatdan o'tganmisiz y/n: ")
        clear_screen()
        if choice == "n":
            username, password = register()
            a.append(username)
            a.append(password)
            clear_screen()
            if len(password) >= 8 and len(password) <= 16 and ("!" in password or "$" in password or "&" in password):
                print("\nTabriklaymiz registratsiyadn muvafaqqiyatli o'tdingiz!!!")
                print(f"Salom {username}")
                note, now = add_note(username)
                za.append(note)
                vaqt.append(now)
            else:
                print("Parol 8 yoki 16 ta belgidan iborat bo'lishi va parolingiz ichida [!, $, &] belgilari bittasi bo'lishi kerak.")
        elif choice == "y":
            username, password = login()
            clear_screen()
            if username in a and password in a:
                print(f"Hush kelibsiz {username}")
                if za:
                    note, now = add_note(username)
                    vaqt.append(now)
                    za.append(note)
                else:
                    print("Hali zametka kiritilmagan.")
            else:
                print("User name yoki parol xato")
        finish = input("\nDastur tugasinmi y/n: ")
        clear_screen()
        if finish == "y":
            break

if __name__ == "__main__":
    main()

