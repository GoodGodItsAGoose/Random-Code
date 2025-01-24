import node as n
import stacks as s
import random as r

stack = s.Stack()
oldStack = s.Stack()

def seperateToList(commaOrNumber):
    paragraph = "The Fool, The Magician, The High Priestess, The Empress, The Emperor, The Hierophant, The Lovers, The Chariot, Strength, The Hermit, Wheel of Fortune, Justice, The Hanged Man, Death, Temperance, The Devil, The Tower, The Star, The Moon, The Sun, Judgement, The World"
    newList = []
    if commaOrNumber == "comma":
        newList = paragraph.split(",")
    return newList

def shuffleCards(deck):
    return r.shuffle(deck)

def insertCardsToStack(deck):
    num = 0
    for _ in range(len(deck)):
        stack.push(deck[num])
        num += 1

def drawCard():
    if r.randint(1,2) == 1:
        print(stack.peek(), " reversed")
    else:
        print(stack.peek(), " upright")
    oldStack.push(stack.peek())
    stack.pop()

def makeCards(number):
    suits = [
        "swords",
        "wands",
        "pentacles",
        "cups"
    ]

    court = [
        "King",
        "Queen",
        "Knight",
        "Page"
    ]
    
    higherCards = seperateToList("comma")
    r.shuffle(higherCards)
    
    num = 1
    num2 = 0
    fullCards = []
    for _ in range(4):
        num = 1
        for _ in range(10):
            if num == 1:
                card = "Ace" + " of " + suits[num2]
            else:
                card = str(num) + " of " + suits[num2]
            
            # if num == 1:
            #     if r.randint(1,3) == 1:
            #         card = "Ace" + " of " + suits[num2] + " reversed"
            #     else:
            #         card = "Ace" + " of " + suits[num2]
            # else:
            #     if r.randint(1,3) == 1:
            #         card = str(num) + " of " + suits[num2] + " reversed"
            #     else:
            #         card = str(num) + " of " + suits[num2]
            
            fullCards.append(card)
            num += 1
        num = 0
        for _ in range(4):
            card2 = court[num] + " of " + suits[num2]
            fullCards.append(card2)
            num += 1
        num2 += 1
    num = 0
    r.shuffle(fullCards)
    cards = fullCards + higherCards
    for _ in range(int(number)):
        r.shuffle(cards)
    for _ in range(len(cards)):
        stack.push(cards[num])
        num += 1

def choice():
    cont = input("input 1 to draw a card or 2 to exit: ")
    if str(cont) == "1":
        drawCard()
    elif str(cont) == "2":
        exit()
        
def startUp():
    cont = input("Input 1 to create a new deck or 2 to exit: ")
    shuffleAmount = input("Input amount of times to shuffle: ")
    if str(cont) == "1":
        makeCards(shuffleAmount)
        choice()
    elif str(cont) == "2":
        exit()
   
cards = [
    "spades",
    "diamonds",
    "hearts",
    "clovers"
]
# stack = Stack()

if __name__ == "__main__":
    startUp()
    while True:
        choice()
            
        
    


