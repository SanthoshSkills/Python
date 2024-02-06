import getpass

db = {"Santhoshkp":"1234", "Santhosh": "5678"}
username = input("Enter username: ")
pwd = getpass.getpass("Enter password: ")
for i in db.keys():
    if username == i:
        while pwd != db.get(i):
            pwd = getpass.getpass("Enter password again: ")
        break
print("Verified")