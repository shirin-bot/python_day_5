import json
try:
    with open("animal.json","r") as f:
        animal=json.load(f)
except FileNotFoundError:
    animal={
        "dog": "domestic",
        "cat": "domestic",
        "rabbit": "domestic",
        "lion": "wild",
        "tiger": "wild"
    }
def save():
    with open("animal.json","w") as f:
        json.dump(animal,f,indent=4)
def add():
    x=input("name:")
    z=input("domestic or wild? ")
    animal[x]=z
    print("added")
    save()
def show():
    for a in animal:
        print(a,animal[a])
        
def search():
    n=input("name:")
    if n in animal:
        print(animal[n])
    else:
        print("not found")

while True:
    y=input("want do you wanth?(search ,add ,show ,exit):")
    if y =="add":
        add()
    elif y=="search":
        search()
    elif y=="show":
        show()
    elif y=="exit":
        print("end")
    else:
        print("Invalid option")
        break
    

    
