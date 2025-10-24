import random
import time

class pet:
    def __init__(self, age, name,):
        self.age = age
        self.name = name
        self.hunger = 50
        self.thrist = 50
        self.happiness = 20
        self.hygiene = 30
        
        
    def feed(self):
            print("------------------------------")
            if self.hunger >= 95:
                print(f"{self.name} is full!!")
            elif self.hunger < 95:
                self.hunger +=5
                self.hygiene -= random.randint(1,5) 
                print(f"{self.name} ate some snacks")
            print("------------------------------")



    def play(self):
        print("------------------------------")
        if self.happiness >= 90:
            return f"{self.name} is happy!"
        elif self.happiness <= 89:
            self.happiness += 10
            print(f"{self.name} played with others!")
            self.hygiene -=  random.randint(1,5) 
            self.hunger -=  random.randint(1,5) 
            self.thrist -=  random.randint(1,5) 
        print("------------------------------")



    def drink(self):
        print("------------------------------")
        if self.thrist >= 90:
            print(f" {self.name} is hydrated!")
        elif self.thrist < 90:
            self.thrist += 4
            print(f"gave {self.name} some water")
            self.happiness -=  random.randint(1,5) 
        print("------------------------------")





    def wash(self):
        print("------------------------------")
        if self.hygiene >= 80:
            print(f"{self.name} is clean!!")
        elif self.hygiene < 80:
            self.hygiene += 10
            print(f"{self.name} jumped in the pool")
            self.hunger -=  random.randint(1,5) 
        print("------------------------------")




age = int(input("How old is your pet: "))
name =input("WHat is your pets name?: ")
userpet = pet(age, name)
while True:
    if userpet.hunger < 0:
        userpet.hunger == 0
        print(f"yo {userpet.name} is hungry")
        time.sleep(2)
    elif userpet.hygiene < 0:
        userpet.hygiene == 0
        print(f"yo {userpet.name} smells")
        time.sleep(2)
    elif userpet.thrist < 0:
        userpet.thrist == 0
        print(f"yo {userpet.name} is THIRSTY")
        time.sleep(2)
    elif userpet.happiness < 0:
        userpet.happiness == 0
        print(f"yo {userpet.name} is BORED")
        time.sleep(2)
    print(f"hunger:{userpet.hunger}, thirst:{userpet.thrist}, hygiene:{userpet.hygiene}, happiness:{userpet.happiness}")
    useraction = input("1 = feed, 2 = give water, 3 = wash, 4 = play:")
    if useraction == "1":
        userpet.feed()
    elif useraction == "2":
        userpet.drink()
    elif useraction == "3":
        userpet.wash()
    elif useraction == "4":
        userpet.play()
    else:
        print("Idiot") 