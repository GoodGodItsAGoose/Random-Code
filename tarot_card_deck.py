import stacks as s
import random as r

stack = s.Stack()
oldStack = s.Stack()

def seperateToList(commaOrNumber):
    paragraph = "The Fool,The Magician,The High Priestess,The Empress,The Emperor,The Hierophant,The Lovers,The Chariot,Strength,The Hermit,Wheel of Fortune,Justice,The Hanged Man,Death,Temperance,The Devil,The Tower,The Star,The Moon,The Sun,Judgement,The World"
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
        card = stack.peek() + " Reversed"
        print(stack.peek(), "Reversed")
    else:
        card = stack.peek() + " Upright"
        print(stack.peek(), "Upright")
    oldStack.push(card)
    stack.pop()

def history():
    listy = []
    defo = True
    while defo == True:
        test = oldStack.peek()
        if test == "Stack is empty.":
            defo = False
        else:
            print(oldStack.peek(), end = " => ")
            listy.append(oldStack.peek())
            oldStack.pop()
    print("None")
    listy = listy[::-1]
    num = 0
    for _ in range(len(listy)):
        oldStack.push(listy[num])
        num += 1

def makeCards(number):
    suits = [
        "Swords",
        "Wands",
        "Pentacles",
        "Cups"
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
    cont = input("input 1 to draw a card, 2 to view the last card, or 3 to exit: ")
    if str(cont) == "1":
        drawCard()
    elif str(cont) == "2":
        history()
    elif str(cont) == "3":
        exit()
        
def startUp():
    cont = input("Input 1 to create a new deck or 2 to exit: ")
    if str(cont) == "1":
        shuffleAmount = input("Input amount of times to shuffle: ")
        makeCards(shuffleAmount)
        choice()
    elif str(cont) == "2":
        exit()

if __name__ == "__main__":
    startUp()
    while True:
        choice()
