# items = [
# { "item":"Iron", "Rarity": "Uncommon"},
# { "item":"Stick","Rarity": "Common"},
# { "item":"Diamond","Rarity": "Uncommon"}
# ]


# craftables = [
#     {"item":"Iron sword","Rarity": "Rare","Recipe":["Iron","Iron","Stick"]},
#     {"item":"Diamond sword","Rarity": "Epic","Recipe":["Diamond","Diamond","Stick"]},
#     {"item":"Diamond Chest plate","Rarity": "Epic","Recipe":["Diamond"]*8}
# ]
# class user():
    
#     def __init__(self,name,invetory):
#         self.name = name
#         self.invetory = invetory if invetory else []
#     def getmats(self, items):
#         for item in items:
#             print(f"{item["item"]}, Rarity:{item["Rarity"]}")

#         while True:
#             print(f"{self.invetory}")
#             userwant = input("What do you want?(to stop type stop):")

#             for item in items:
#                 if userwant.upper() == item["item"].upper():
#                     self.invetory.append(userwant)
#                     print(f"Added {item}!")
#             if userwant == "stop":
#                 print("invetory")
#                 for thing in self.invetory:
#                     print(thing)
#                 break
#     def craft(self):
#         for craft in craftables:
#             print(f"{craft["item"]}")
#             print("------------------------")
#             for craftitem in craft["Recipe"]:
#                 print(craftitem)
#             print("------------------------")


#         userwant = input("What do you wanna craft?: ")
        
#         selected = None
            
#         for crafts in craftables:
#             if userwant.lower() == crafts["item"].lower():
#                 selected = crafts
#         if selected == None:
#             print("Item not in recipe")
#             return
        
#         hasreq = all(req in self.invetory for req in selected["Recipe"])
#         if hasreq == True:
#             for required_item in selected["Recipe"]:
#                 self.invetory.remove(required_item)
#             self.invetory.append(selected["item"])

#             for item in self.invetory:
#                 print(f"You crafted {selected["item"]}")
#             print(f"{self.invetory}")
#         else:
#             print("no required items dood")



from tkinter import *


window = Tk()
window.geometry("600x600")
window.title("Clicker Game!")

multiplyer = 1
number = 0 

def clicker():
    global number
    number += 1 * multiplyer
    infoshower.config(text = number)
def upgrade():
    global number
    global multiplyer
    if number > 100 * 2 * multiplyer:
        multiplyer += 1
        number -= 100 
    multiplyershow.config(text = multiplyer)
    
clickingbutton = Button(window,text="click!", padx=50, pady=50, bg="gold", font=("Arial, 22"), command=clicker)

infoshower = Label(window,text=number, padx =100, pady = 100, font="Arial, 30")
multiplyershow = Label(window,text = multiplyer, padx = 20, pady = 20, font = "Arial, 15")
upgradebutton = Button(window, text = "Upgrade!", padx = 25, pady = 25, font =("Arial","15"), command = upgrade)


infoshower.pack() 

clickingbutton.pack()
upgradebutton.pack()
multiplyershow.pack()
window.mainloop()
