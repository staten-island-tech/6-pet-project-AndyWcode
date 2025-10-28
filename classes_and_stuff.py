items = [
{ "item":"Iron", "Rarity": "Uncommon"},
{ "item":"stick","Rarity": "Common"},
{ "item":"Diamond","Rarity": "Uncommon"}
]


craftables = [
    {"item":"Iron sword","Rarity": "Rare","Recipe":"Iron, Iron, Stick"},
    {"item":"Diamond sword","Rarity": "Epic","Recipe":"Diamond, Diamond, Stick"},
    {"item":"Diamond Chest plate","Rarity": "Epic","Recipe":"Diamond,Diamond,Diamond,Diamond,Diamond,Diamond,Diamond,Diamond"}
]
class user():
    
    def __init__(self,name,invetory):
        self.name = name
        self.invetory = [invetory]
    def getmats(self):
        for item in items:
            print(f"{item["item"]}, Rarity:{item["Rarity"]}")
        while True:
            userwant = input("What do you want?(to stop type stop):")
            for item in items:
                if userwant.upper() == item["item"].upper():
                    self.invetory.append(userwant)
            if userwant == "stop":
                print("invetory")
                for thing in self.invetory:
                    print(thing)
                break
    def craft(self):
        for crafts in craftables:
            print(f"{crafts["item"]}, Recipe:{crafts["Recipe"]}")
        usercraft = input("What do you wanna craft?")

Andy = user("Andy",["Iron, stick"])
        
user.craft(Andy)