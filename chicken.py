import random
import pygame
gameover = False
class Chicken:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        
    def update(self):
        self.hunger += 5
        if self.hunger > 30:
            if random.randrange(1,100) > 50:
                print("Bok bok")
                return 1
        else:
            return 0
    
    def feed(self,x):
        self.hunger -= x
        print ("peck peck")
        
    def pet(self):
        print ("happy noices")
    
    def printinfo(self):
        print(self.name)
        print(self.hunger)
#end of class chicken---------------------------------------

numEggs = 0
    
c1 = Chicken("e")
c2 = Chicken("j")
c3 = Chicken("brandon")

while not gameover:

    print ("what do you want to do to your Chicken, (p)et (f)eed or print(i)nfo")
    w = input()
    
    if w == "f":
        hungry = int(input("enter amount to feed"))
        c2.feed(hungry)
        c1.feed(hungry)
        c3.feed(hungry)
      
    
    elif w == "p":
        c1.pet()
        c2.pet()
        c3.pet()
        
    elif w == "i":
        c1.printinfo()
        c2.printinfo()
        c3.printinfo()
        
    numEggs+=c1.update()
    numEggs+=c2.update()
    numEggs+=c3.update()
    
    
pygame.quit
