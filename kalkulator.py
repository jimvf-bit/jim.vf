import os

os.system("clear")
print("\t\t\t>>>>>>>>>< Calculator ><<<<<<<<<")


def match():
    while True:
        amal = input("Enter an example: ")
        if amal == 'q':
            break

        natija = eval(amal)

        print(f"Answer: {natija}")


try:
    match()
except:
    print("Enter the correct actions")
match()
