import random
def Move(Player, value):
    snakes = {16: 4, 22:10, 33: 20, 48: 24, 62: 56, 78: 69, 74: 60, 91: 42, 97: 6}
    ladder = {3: 12, 7: 23, 11:25, 21: 56, 47: 53, 60: 72, 80: 96}
    Throw = random.randint(1, 6)
    num = value + Throw
    if num>100:
        print("BAD LUCK, YOU CANT MOVE, YOU NEED A {} TO WIN".format(100 - value))
        return value
    if num == 100:
        return num
    #IF NONE OF THE OTHER CONDITIONS ARE MATCHED,
    print(Player, "Rolled", Throw, "now your score is", num, "\n")
    if num in snakes:
        #if landed in a snake square
        print(Player, "got bitten by a snake and is now your score is", snakes[num])
        num = snakes[num]
    elif num in ladder:
        #if landed in a ladder square
        print(Player, " YOU GOT A LADDER ", ladder[num])
        num = ladder[num]

    return num

def playerscount():
    """ACCEPTS THE NUM OF PLAYERS"""
    numofplayers = int(input("ENTER NUMBER OF PLAYERS: "))
    print()
    if numofplayers > 4 or numofplayers < 2:
        print("MUST BE LESS THAN 5 AND GREATER THAN 1 ")
    else:
        return numofplayers


def nameofplayers(N):
    """ACCEPTS THE NAME OF PLAYERS AND REUTUNS THE LIST OF NAMES"""
    Names = ['','','','']
    for i in range(N):
        Names[i] = input("ENTER PLAYER NAME:"+str(i+1)+" ")
    return Names

def turn(player,pos):
    COMMANDSTATE = "PRESS ENTER TO ROLL THE DICE" 
    WINSTATEMENT = "YOU WIN THE GAME! CONGRATULATIONS"
    COMMANDSTATE1 = str(" "+player+" ITS YOUR TURN "+COMMANDSTATE)
    Command = input(COMMANDSTATE1)
    if Command.lower() == 'stop':
        #if the user commands to stop, the game must stop,
        #so the GameOver flag will become true
        return True, pos
    pos = Move(player, pos)
    if pos == 100:
        print("{} YOUR SCORE IS {}".format(player, pos))
        print(player, WINSTATEMENT)                         
        #if a player wins, the game is over
        #so the GameOver flag will become true
        return True, pos
        
    #if the function has not returned anywhere above
    #it means that the game is still on
    return False, pos
def main():
    """THE MAIN FUNCTION"""
    numofplayers = playerscount()
    playernames = nameofplayers(numofplayers)
    print(playernames[0], playernames[1], playernames[2], playernames[3],"NOW PLAYING SNAKE AND LADDER GAME")
    COMMANDSTATE = ""
    WINSTATEMENT = "WINS THE GAME! CONGRATULATIONS"
    # Command = 'ABC'
    TURNS = 0
    PosArr=[1,1,1,1]
    #A list containing the present positions of the pawns
    GameOver = False
    #Flag to check whether the game should be continued or not
    while not GameOver:      
        while TURNS < numofplayers:
            #This loops takes care of each person's moves.
            #if TURNS == 1, it means that its person1's turn
            TURNS += 1
            GameOver, PosArr[TURNS - 1] = turn(playernames[TURNS - 1], PosArr[TURNS - 1])
            if GameOver:
                #if gameover, exit the function
                return
        TURNS = 0
    return
if __name__=='__main__':
    main()