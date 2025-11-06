import random


class pet:
    def __init__(self, age, name,):
        self.age = age
        self.name = name
        self.hunger = random.randint(40, 60)
        self.thrist = random.randint(30, 60)
        self.happiness = random.randint(20, 40)
        self.hygiene = random.randint(30,50)

        
        
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
            self.happiness -=  random.randint(1,9) 
        print("------------------------------")





    def wash(self):
        print("------------------------------")
        if self.hygiene >= 80:
            print(f"{self.name} is clean!!")
        elif self.hygiene < 80:
            self.hygiene += 10
            print(f"{self.name} jumped in the pool")
            self.hunger -=  random.randint(1,9) 
        print("------------------------------")





def maingame(userpet):
        
        action = 0
        game = True
        while game:
                
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
                action +=1
                if userpet.hunger <= 0  or userpet.thrist <= 0:
                    game = False
        print(f"{userpet.name} is dead")
        print(f"you did {action} actions before {userpet.name} died")

def verifyandstuff():

    while True:
        age = input("How old is your pet: ")
        if age.isdigit():
            name = input("give your pet a name")
            userpet = pet(age, name)
            break
            
        else:
            print("age has to be a integer or ur pet is too young")
    maingame(userpet)
        

verifyandstuff()