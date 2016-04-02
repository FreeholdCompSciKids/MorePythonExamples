
myMoney = 1000000

myStuff = {}
myStuff['lemonade'] = 1000
myStuff['oil'] = 2000
myStuff['video games'] = 500
myStuff['dentures'] = 500

moneyWeGet = {}
moneyWeGet['lemonade'] = 0.03
moneyWeGet['oil'] = 0.10
moneyWeGet['video games'] = 0.04
moneyWeGet['dentures'] = 0.01

prices = {}
prices['lemonade'] = 10
prices['oil'] = 200000
prices['video games'] = 30000
prices['dentures'] = 200

def printMyStuff():
    # print my money and my stuff
    print "----------------------------"
    print " My Money: $", myMoney
    print "----------------------------"
    print " My stuff:"
    for s in myStuff:
        print "    ", s, ":", myStuff[s] 
    print "----------------------------"

def buyStuff():
    

def run():
    global myMoney
    for i in range(20):
        printMyStuff()
        
        #compute how much more $ i have
        for s in myStuff:
            myMoney +=  myStuff[s] * moneyWeGet[s]

        #now let's buy some stuff
        buyStuff()
   

#============================
# program starts here

run()
