def robin_hood(money):
    if money in range (0,101):
        money = money*2
        print ("Dar")
        print ("Konecny stav:", money)
    else:
        if money not in range (0,101):
            money = money-50
            print ("Lup")
            print ("Konecny stav:", money)
