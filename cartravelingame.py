import random as r
import time as t

class driving:
    def __init__(self):
        self.checkpoints = 0
        self.checkpointDistance = []
        self.currentDistance = 0
        self.currentCheckPoint = 0
        self.nextCheckPoint = 0
        self.checkpointsPassed = []
        self.difficulty = None
        self.gasLevel = r.randint(85, 115)
        self.money = 1500
        self.gasPrice = r.randint(22, 43)/10
        self.miles = 0
        self.distanceToNextCheckpoint = 0
        self.multiplier = 1
        self.distanceMultiplier = 1
        self.moneyMultiplier = 1.15
    
    def roundup(self, x):
        return round(x, 2)

    def setDifficulty(self):
        difficulty = input("Enter difficulty level (1-3): ")
        num = 1
        for _ in range(3):
            if difficulty == str(num):
                self.difficulty = int(difficulty)
                self.money = self.money // self.difficulty
                return
            else:
                num += 1
        print("Please re-enter your difficulty choice.")
        self.setDifficulty()

        
    def checkPassedCheckpoint(self):
        if self.checkpointDistance[self.nextCheckPoint-1] <= self.currentDistance:
            print()
            t.sleep(.3)
            print(f"You reached checkpoint {self.checkpoints}.")
            t.sleep(.3)
            self.makeCheckPoints()
            self.addMoneyFromCheckpoint()
            t.sleep(.3)
            print()
            self.gasLevelCheck()
    
    def addMoneyFromCheckpoint(self): 
        payment = r.randint(120, 365) * self.difficulty * self.moneyMultiplier
        benefits = r.randint(1,45)
        benefits = 1+(benefits / 100)
        payment = self.roundup(payment * benefits)
        self.money += payment
        self.money = self.roundup(self.money)
        print(f"You gained {payment} dollars from reaching a checkpoint! You now have {self.money} dollars.")
        t.sleep(.3)

    def addMoneyFromMiles(self):
        payment = r.randint(15, 35) * self.difficulty * self.moneyMultiplier
        if payment >= 65:
            payment += r.randint(20,30)
        benefits = r.randint(1,25)
        benefits = 1+(benefits / 100)
        payment = self.roundup(payment * benefits)
        self.money += payment
        self.money = self.roundup(self.money)
        print(f"You gained {payment} dollars from driving! You now have {self.money} dollars.")
        t.sleep(.3)

    def Meteorite(self):
        cost = r.randint(850,1250) * (self.moneyMultiplier +(0.05/self.nextCheckPoint))
        cost = self.roundup(cost)
        print(f"A meteorite hit your car! You must pay {cost} dollars in damages.")
        t.sleep(.3)
        self.moneyCheck(cost)

    def Breakdown(self):
        cost = r.randint(350,720) * (self.moneyMultiplier +(0.05/self.nextCheckPoint))
        cost = self.roundup(cost)
        print("You broke down!")
        t.sleep(.3)
        print(f"You paid {cost} dollars to repair.")
        t.sleep(.3)
        self.moneyCheck( cost)

            
         #also add an option to wait
        
    def moneyCheck(self, cost):
        self.money = self.roundup(self.money - cost)
        if self.money < 0:
            print(f"You're now {-self.money} dollars in debt.")
            t.sleep(.3)
        else:
            print(f"You now have {self.money} dollars left.")
            t.sleep(.3)
    
    def RanARedLight(self):
        copChance = r.randint(1,3)
        if copChance == 3:
            cost = r.randint(25,45) * (self.moneyMultiplier +(0.05/self.nextCheckPoint))
            cost = self.roundup(cost)
            print(f"You ran a red light and got caught by a cop! You had to pay {cost} in fines.")
            t.sleep(.3)
            self.moneyCheck( cost)
            
            # skip turns, get ticket, must pay, (per checkpoint you pass you get money)
        else:
            return None

    def fenderBender(self):
        cost = r.randint(50,150) * (self.moneyMultiplier +(0.05/self.nextCheckPoint))
        cost = self.roundup(cost)
        print(f"You got into a fender bender. You had to pay {cost} dollars.")
        t.sleep(.3)
        self.moneyCheck( cost)
        

    def RefillGas(self):
        if self.gasLevel >= r.randint(10,20):
            return None
        else:
            print("Time to refill the gas!")
            cost = self.roundup(self.gasPrice * (-(self.gasLevel-100)))
            self.gasLevel = 100
            print(f"You refilled your gas and paid {cost} dollars.")
            t.sleep(.3)
            self.moneyCheck(cost)

    def toll(self):
        cost = r.randint(15,125) * (self.moneyMultiplier +(0.05/self.nextCheckPoint))
        cost = self.roundup(cost)
        print(f"You passed a toll and had to pay {cost} dollars!")
        t.sleep(.3)
        self.moneyCheck(cost)
    
    def hitAndRun(self):
        cost = r.randint(150,420) * (self.moneyMultiplier +(0.05/self.nextCheckPoint))
        cost = self.roundup(cost)
        print(f"You accidentally ran into someone's car and had to pay {cost} dollars!")
        t.sleep(.3)
        self.moneyCheck(cost)

    def FlatTire(self): 
        cost = r.randint(15,35) * (self.moneyMultiplier +(0.05/self.nextCheckPoint))
        cost = self.roundup(cost)
        print(f"You got a flat tire! You must pay {cost} dollars.")
        self.moneyCheck(cost)

    def gasLevelCheck(self):
        if self.gasLevel > 10:
            return
        else:
            self.RefillGas()

    def you_got_hungry(self):
        burger_amount = r.randint(1, 4)
        fries_amount = r.randint(1,3)
        shake_amount = r.randint(1,4)
        burgers = ["a single patty hamburger", "a double quarter pound cheeseburger", "a chicken burger", "the GOD burger"]
        fries = ["small fry", "medium fry", "large fry"]
        shakes = ["strawberry", "chocolate", "vanilla", "money"]
        burger_costs = [6.50, 12.65, 9.45, 32.60]
        fries_cost = [2.50, 3.25, 4.75]
        shakes_cost = [5.30, 5.30, 5.30, 46.75]
        cost = burger_costs[burger_amount-1] + fries_cost[fries_amount-1] + shakes_cost[shake_amount-1]
        print(f"You got hungry and stopped at a burger place! You got {burgers[burger_amount-1]}, a {fries[fries_amount-1]}, and a {shakes[shake_amount-1]} shake. It cost you {str(cost)} dollars.")
        t.sleep(.3)
        self.moneyCheck(cost)

    def human_x_car(self):
        cost = r.randint(119500, 184599)/100
        print(f"You hit someone! You have to pay {str(cost)} dollars in damages.")
        self.moneyCheck(cost)

    # burger

    # ran over person

    def priceChange(self):
        change = r.randint(1,5)
        chance = r.randint(1,60)
        if change == r.randint(2,3) and self.gasPrice < 7.64:
            inflation = (312 / r.randint(87,294)) / 12
            self.gasPrice = self.gasPrice * 1+inflation
            self.gasPrice = self.roundup(self.gasPrice)
            print(f"Gas prices changed, it now costs {self.gasPrice} dollar(s) per unit of fuel.")
        elif chance == r.randint(1,2) and self.gasPrice > 2.1:
            inflation = (312 / r.randint(87,294)) / 12
            self.gasPrice = self.gasPrice - (self.gasPrice * inflation)
            self.gasPrice = self.roundup(self.gasPrice)
            print(f"Gas prices changed, it now costs {self.gasPrice} dollar(s) per unit of fuel.")

    # lose time

    def Nothing(self):
        return None

    def didSomethingHappen(self):
        self.gasLevelCheck()
        chance = r.randint(0,100)
        happenings = [0, 21, 36, 45, 53, 68, 79, 87, 92, 99, 100]
        num = 0
        stuff = [self.Nothing, self.toll, self.you_got_hungry, self.RanARedLight, self.fenderBender, self.FlatTire, self.Breakdown, self.hitAndRun, self.Meteorite, self.human_x_car]
        pos1 = 0
        pos2 = 1
        for _ in range(10):
            if chance >=happenings[pos1] and chance <= happenings[pos2]:
                if stuff[num]() == None:
                    pass
                else:
                    print(stuff[num]())
                return
            else:
                pos1 += 1
                pos2 += 1
                num += 1
    

    def makeCheckPoints(self):
        num = 1
        distance = r.randint(5,12)
        for _ in range(3):
            self.multiplier += .05
            if self.difficulty == num:
                distance = self.currentDistance + r.randint(6,12) + (r.randint(2,3) * self.difficulty) * self.multiplier
                distance = round(distance)
                self.checkpointDistance.append(int(distance))
                self.multiplier += self.roundup(r.randint(10,20)/100)
                self.checkpoints += 1
                self.nextCheckPoint += 1
                return
            else:
                num += 1
        
    
    def tickUpOne(self):
        
        if self.currentCheckPoint % 2 == 0:
            self.distanceMultiplier += self.roundup(r.randint(1,5)/100)
            if r.randint(1,2) == 2:
                self.moneyMultiplier += self.roundup(r.randint(1, 5)/100)
        distance = r.randint(1,5) * self.distanceMultiplier
        distance = round(distance)
        print()
        t.sleep(.15)

        self.currentDistance += distance

        self.checkPassedCheckpoint()
        if self.currentCheckPoint == self.checkpoints:
            self.makeCheckPoints()
        print()
        t.sleep(.15)
        
        if self.money <= -2745:
            print("You went into so much debt you died from loan sharks catching you!")
            t.sleep(.3)
            exit()
        if self.money > 13500:
            print("You became too rich and posh to drive! Game over!")
            t.sleep(.3)
            exit()
        self.distanceToNextCheckpoint = self.checkpointDistance[self.nextCheckPoint - 1] - self.currentDistance
        self.gasLevel -= distance
        t.sleep(.3)
        print(f"You drove {distance} unit(s) of travelling further! You have {self.distanceToNextCheckpoint} more units of travel to traverse until the next checkpoint, {self.money} dollars left, and {self.gasLevel} units of gas left.")
        t.sleep(.3)
        if r.randint(1,14+self.difficulty) >= 14+round(self.difficulty):
            self.addMoneyFromMiles()
            t.sleep(.3)
        if r.randint(1,5) == r.randint(1,4):
            self.priceChange()
            t.sleep(.3)
        if r.randint(1,3) <= 2 or self.gasLevel <= 10:
            t.sleep(.3)
            self.didSomethingHappen()
            if r.randint(1,4) == r.randint(1,4):
                t.sleep(.3)
                self.didSomethingHappen()
            if r.randint(1,6) == r.randint(1,8):
                t.sleep(.3)
                self.didSomethingHappen()
            t.sleep(.3)
    
    def printDistances(self):
        print(self.checkpointDistance)
        print(self.nextCheckPoint)

c = driving()
c.setDifficulty()
c.makeCheckPoints()

if __name__ == "__main__":
    while True:
        c.tickUpOne()
        exit2 = input("Enter '1' to exit, or press enter to continue. ")
        if exit2 == "1":
            exit()
