import datetime
startTime = datetime.datetime.now()
print("---------------------------------")
print("GENERATING HTML-ONLY TIC-TAC-TOE")
print("---------------------------------")
print("TIME STARTED: " + str(startTime))
print("---------------------------------")

def changePlayer(player):
    if(player == 1):
        return 2
    else:
        return 1

def getSymbol(player):
    if(int(player) == 1):
        return "o"
    else:
        return "x"

def calcFileName(line0, line1, line2, nextplayer):
    return line0 + line1 + line2 + nextplayer

template = """<html>
<header><title>TIC TAC TOE</title></header>
<body>

<a href="ref00.html">
  <img src="type00.png" alt="ref00">
</a>
<a href="ref01.html">
  <img src="type01.png" alt="ref01">
</a>
<a href="ref02.html">
  <img src="type02.png" alt="ref02">
</a>

<br>

<a href="ref10.html">
  <img src="type10.png" alt="ref10">
</a>
<a href="ref11.html">
  <img src="type11.png" alt="ref11">
</a>
<a href="ref12.html">
  <img src="type12.png" alt="ref12">
</a>

<br>

<a href="ref20.html">
  <img src="type20.png" alt="ref20">
</a>
<a href="ref21.html">
  <img src="type21.png" alt="ref21">
</a>
<a href="ref22.html">
  <img src="type22.png" alt="ref22">
</a>

<p>MESSAGE</p>

</body>
</html>"""

restartButton = """<p>
<a href="0000000001.html">
  <img src="restart.png" alt="restart">
</a>
</p>"""

calculatedStates = set({})
statesToGenerate = set({})

statename = "0000000001"

line0 = "000"
line1 = "000"
line2 = "000"

player = 1


while(True):
    if(statename in calculatedStates):
        continue

    state = template
    state = state.replace("type00", "empty" if line0[0] == "0" else line0[0])
    state = state.replace("type01", "empty" if line0[1] == "0" else line0[1])
    state = state.replace("type02", "empty" if line0[2] == "0" else line0[2])

    state = state.replace("type10", "empty" if line1[0] == "0" else line1[0])
    state = state.replace("type11", "empty" if line1[1] == "0" else line1[1])
    state = state.replace("type12", "empty" if line1[2] == "0" else line1[2])

    state = state.replace("type20", "empty" if line2[0] == "0" else line2[0])
    state = state.replace("type21", "empty" if line2[1] == "0" else line2[1])
    state = state.replace("type22", "empty" if line2[2] == "0" else line2[2])

    nextPlayer = str(changePlayer(player))
    names = []
    names.append(calcFileName((line0[0] if line0[0] != "0" else getSymbol(nextPlayer)) + line0[1] + line0[2], line1, line2, nextPlayer))
    names.append(calcFileName(line0[0] + (line0[1] if line0[1] != "0" else getSymbol(nextPlayer)) + line0[2], line1, line2, nextPlayer))
    names.append(calcFileName(line0[0] + line0[1] + (line0[2] if line0[2] != "0" else getSymbol(nextPlayer)), line1, line2, nextPlayer))

    names.append(calcFileName(line0, (line1[0] if line1[0] != "0" else getSymbol(nextPlayer)) + line1[1] + line1[2], line2, nextPlayer))
    names.append(calcFileName(line0, line1[0] + (line1[1] if line1[1] != "0" else getSymbol(nextPlayer)) + line1[2], line2, nextPlayer))
    names.append(calcFileName(line0, line1[0] + line1[1] + (line1[2] if line1[2] != "0" else getSymbol(nextPlayer)), line2, nextPlayer))

    names.append(calcFileName(line0, line1, (line2[0] if line2[0] != "0" else getSymbol(nextPlayer)) + line2[1] + line2[2], nextPlayer))
    names.append(calcFileName(line0, line1, line2[0] + (line2[1] if line2[1] != "0" else getSymbol(nextPlayer)) + line2[2], nextPlayer))
    names.append(calcFileName(line0, line1, line2[0] + line2[1] + (line2[2] if line2[2] != "0" else getSymbol(nextPlayer)), nextPlayer))

    state = state.replace("ref00", names[0] if line0[0] == "0" else statename)
    state = state.replace("ref01", names[1] if line0[1] == "0" else statename)
    state = state.replace("ref02", names[2] if line0[2] == "0" else statename)

    state = state.replace("ref10", names[3] if line1[0] == "0" else statename)
    state = state.replace("ref11", names[4] if line1[1] == "0" else statename)
    state = state.replace("ref12", names[5] if line1[2] == "0" else statename)

    state = state.replace("ref20", names[6] if line2[0] == "0" else statename)
    state = state.replace("ref21", names[7] if line2[1] == "0" else statename)
    state = state.replace("ref22", names[8] if line2[2] == "0" else statename)
    
    if(line0[0] == line0[1] and line0[1] == line0[2] and line0[0] != "0"):
        if(line0[0] == "x"):
            state = state.replace("MESSAGE", "PLAYER 'X' WON! " + restartButton)
        else:
            state = state.replace("MESSAGE", "PLAYER 'O' WON! " + restartButton)
    elif(line1[0] == line1[1] and line1[1] == line1[2] and line1[0] != "0"):
        if(line1[0] == "x"):
            state = state.replace("MESSAGE", "PLAYER 'X' WON! " + restartButton)
        else:
            state = state.replace("MESSAGE", "PLAYER 'O' WON! " + restartButton)
    elif(line2[0] == line2[1] and line2[1] == line2[2] and line2[0] != "0"):
        if(line2[0] == "x"):
            state = state.replace("MESSAGE", "PLAYER 'X' WON! " + restartButton)
        else:
            state = state.replace("MESSAGE", "PLAYER 'O' WON! " + restartButton)


    elif(line0[0] == line1[0] and line1[0] == line2[0] and line0[0] != "0"):
        if(line0[0] == "x"):
            state = state.replace("MESSAGE", "PLAYER 'X' WON! " + restartButton)
        else:
            state = state.replace("MESSAGE", "PLAYER 'O' WON! " + restartButton)
    elif(line0[1] == line1[1] and line1[1] == line2[1] and line0[1] != "0"):
        if(line0[1] == "x"):
            state = state.replace("MESSAGE", "PLAYER 'X' WON! " + restartButton)
        else:
            state = state.replace("MESSAGE", "PLAYER 'O' WON! " + restartButton)
    elif(line0[2] == line1[2] and line1[2] == line2[2] and line0[2] != "0"):
        if(line0[2] == "x"):
            state = state.replace("MESSAGE", "PLAYER 'X' WON! " + restartButton)
        else:
            state = state.replace("MESSAGE", "PLAYER 'O' WON! " + restartButton)


    elif(line0[0] == line1[1] and line1[1] == line2[2] and line0[0] != "0"):
        if(line0[0] == "x"):
            state = state.replace("MESSAGE", "PLAYER 'X' WON! " + restartButton)
        else:
            state = state.replace("MESSAGE", "PLAYER 'O' WON! " + restartButton)
    elif(line0[2] == line1[1] and line1[1] == line2[0] and line0[2] != "0"):
        if(line0[2] == "x"):
            state = state.replace("MESSAGE", "PLAYER 'X' WON! " + restartButton)
        else:
            state = state.replace("MESSAGE", "PLAYER 'O' WON! " + restartButton)
    elif("0" not in line0 and "0" not in line1 and "0" not in line2):
        state = state.replace("MESSAGE", "DRAW " + restartButton)
    elif(player == 1):
        state = state.replace("MESSAGE", "Player 'X' turn")
    else:
        state = state.replace("MESSAGE", "Player 'O' turn")

    statesToGenerate.update(names)

    with open('{}.html'.format(statename), 'w') as file:
        file.write(state)

    calculatedStates.update(statename)

    statename = statesToGenerate.pop()
    line0 = statename[:3]
    line1 = statename[3:6]
    line2 = statename[6:9]
    player = int(statename[9])

    print("States in queue: " + str(len(statesToGenerate)))

