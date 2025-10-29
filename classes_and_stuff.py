items = [
{ "item":"Iron", "Rarity": "Uncommon"},
{ "item":"Stick","Rarity": "Common"},
{ "item":"Diamond","Rarity": "Uncommon"}
]


craftables = [
    {"item":"Iron sword","Rarity": "Rare","Recipe":["Iron","Iron","Stick"]},
    {"item":"Diamond sword","Rarity": "Epic","Recipe":["Diamond","Diamond","Stick"]},
    {"item":"Diamond Chest plate","Rarity": "Epic","Recipe":["Diamond","Diamond","Diamond","Diamond","Diamond","Diamond","Diamond",]}
]
class user():
    
    def __init__(self,name,invetory):
        self.name = name
        self.invetory = invetory if invetory else []
    def getmats(self, items):
        for item in items:
            print(f"{item["item"]}, Rarity:{item["Rarity"]}")

        while True:
            print(f"{self.invetory}")
            userwant = input("What do you want?(to stop type stop):")

            for item in items:
                if userwant.upper() == item["item"].upper():
                    self.invetory.append(userwant)
                    print(f"Added {item}!")
            if userwant == "stop":
                print("invetory")
                for thing in self.invetory:
                    print(thing)
                break
    def craft(self):
        for craft in craftables:
            print(f"{craft["item"]}")
            print("------------------------")
            for craftitem in craft["Recipe"]:
                print(craftitem)
            print("------------------------")
            
me = user("Andy",["Iron","Stick"])
me.craft()