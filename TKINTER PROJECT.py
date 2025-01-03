#Submitted on April 22, 2021
#Import Statements
from tkinter import * 
from pygame import mixer
import random
#Global Variables (Font, Canvas Size, etc.)
canvasHeight = 1100
canvasWidth = 1650 
bgImageA = 875 
bgImageB = 550 
textFont = 'Bahnschrift'
#-------------------------------------------------
#Function for Instruction Canvas
def goinst():
    instRoot = Tk()
    instScreen = Canvas(instRoot, height = 300, width = 1300, bg = 'bisque')
    instScreen.pack()
    instHeader = instScreen.create_text(650, 75, text = 'Welcome to the 2021 NBA Draft', font = (textFont, '23'), anchor = CENTER)                                                                                                                                                                                        
    instructions = "With a regular-season record below .300, your team has been allocated the first pick in this year's draft. \nAs the GM of your team, you have the executive decision of drafting a single player from the first-round candidate pool. \nYou will have the opportunity to select a player and subsequently accept/decline an incoming trade request from another draft-participant team. \nMulti-player trades may not be initiated; pre-drafted/undrafted players holding active contracts may not be included in any proposed offers.\nYou will then negotiate a contract price with the selected player. Once a negotiation has been made, the player will officially join your orginization" 
    instText = instScreen.create_text(650, 200, text = instructions, font = (textFont, '9'), anchor = CENTER)
    mainloop()
#Function for recieving input from widgets and proceeding
def toScreen2():
    global playerName, playerTeam
    #Recieving input from entry-box and option-menu
    playerName = name.get()
    playerTeam = team.get()
    teamsList.remove(playerTeam)
    mixer.music.stop()
    root.destroy()
#Creating canvas for intro screen
root = Tk()
introScreen = Canvas(root, height = canvasHeight, width = canvasWidth)
introScreen.pack()
#Configuring cursor
root.config(cursor = 'circle')
#Setting background image
bgImage = PhotoImage(file = 'introbg.gif')
introImage = introScreen.create_image(bgImageA, bgImageB, image = bgImage)
#Playing audio using pygame mixer
mixer.init()
mixer.music.load("NBA.mp3")
mixer.music.set_volume(100)
mixer.music.play(-1)
#Logo image creation (header)
logo = PhotoImage(file = 'nbadraftlogo.gif')
introLogo = introScreen.create_image(800, 150, image = logo)
#Creating entry-box for name input
enterName = introScreen.create_text(800, 450, text = 'Enter Name', fill = 'white', font = (textFont, '32'))
name = StringVar()
nameEntry = Entry(root, textvariable = name)
introEntry = introScreen.create_window(800, 525, window = nameEntry)
#Creating option-menu widget for team selection (FUNCTION 1/2)
enterTeam = introScreen.create_text(800, 750, text = 'Select Team', fill = 'white', font = (textFont, '32'))
teamsList = ['Toronto Raptors', 'Golden State Warriors', 'Los Angeles Lakers', 'Houston Rockets', 'San Antonio Spurs', 'Phoenix Suns', 'Milwaukee Bucks', 'Charlotte Hornets', 'Miami Heat']
team = StringVar()
teamsOpt = OptionMenu(root, team, *teamsList)
teamsSelect = introScreen.create_window(800, 850, window = teamsOpt)
#Creating proceed/instruction button with appropriate size/positioning
proceedB = Button(root, text = "Proceed", width = 10, height = 2, cursor = 'target', command = toScreen2)
proceedButton = introScreen.create_window(1590, 1060, window = proceedB)
instructionsB = Button(root, text = "Instructions", width = 10, height = 2, cursor = 'target', command = goinst)
intructionsButton = introScreen.create_window(65, 1060, window = instructionsB)

root.mainloop()

#----------------------------------------------------------------------
#Creating canvas for draft screen
root1 = Tk()
draftScreen = Canvas(root1, height = canvasHeight, width = canvasWidth)
draftScreen.pack()
#Configuring cursor
root1.config(cursor = 'circle')
#Playing audio using pygame mixer
mixer.music.load("beat.mp3")
mixer.music.set_volume(100)
mixer.music.play(-1)
#Setting background image
secondBgImage = PhotoImage(file = 'draftbg.gif')
secondBg = draftScreen.create_image(825, bgImageB, image = secondBgImage)
#Creating header text
draftHeader = '{}, Select a Player to Draft'.format(playerName)
selectPick = draftScreen.create_text(825, 100, text = draftHeader, fill = 'white', font = (textFont, '45'))
selectPT = 'Click On a Player to Select'
selectPText = draftScreen.create_text(825, 1000, text = selectPT, fill = 'white', font = (textFont, '23'))
#--------------------------------
#Collection of lists (players/files) to be used in subsequent functions, as well as generating the randomized draft pool
pList = ['Giannis Antetokounmpo','Lamelo Ball','Ja Morant','Zion Williamson','Kawhi Leonard','Stephen Curry','Lebron James','Kevin Durant','Anthony Edwards']
fileList = ['giannis.gif','melo.gif','ja.gif','zion.gif','kawhi.gif','curry.gif','bron.gif','kd.gif','ant.gif']
pSelect = []
payFileList = []
playerSelectList = []
pOneList = ['Giannis Antetokounmpo', 'Lamelo Ball', 'Ja Morant'] 
pOne = random.choice(pOneList)
pTwoList = ['Zion Williamson','Kawhi Leonard','Stephen Curry']
pTwo = random.choice(pTwoList)
pThreeList = ['Lebron James','Kevin Durant','Anthony Edwards']
pThree = random.choice(pThreeList)
#---------------------------------
#Functions for determining the selected player and proceeding
def pOneSelect():
    mixer.music.stop()
    pSelect.append(pOne)
    root1.destroy()
def pTwoSelect():
    mixer.music.stop()
    pSelect.append(pTwo)
    root1.destroy()
def pThreeSelect():
    mixer.music.stop()
    pSelect.append(pThree)
    root1.destroy()
#Function for stat screen for first player in generated pool
def statCommand():
    #Setting canvas attributes for each individual player upon generation
    if pOne == 'Giannis Antetokounmpo':
        stat1Bg = 'PaleGreen4'
        pos1 = 'SF'
        star1 = '5 ★★★★★'
        ppg1 = 28.8
        rpg1 = 11.4
        apg1 = 6.2
    elif pOne == 'Lamelo Ball':
        stat1Bg = 'dark turquoise'
        pos1 = 'PG'
        star1 = '4 ★★★★'
        ppg1 = 15.9
        rpg1 = 5.9
        apg1 = 6.1
    else:
        stat1Bg = 'DodgerBlue4'
        pos1 = 'PG'
        star1 = '4 ★★★★'
        ppg1 = 19.0
        rpg1 = 3.5
        apg1 = 7.4
    #Formatting stat text to include previously set variables  
    ppg1text = 'PPG: {}'.format(ppg1)
    rpg1text = 'RPG: {}'.format(rpg1)
    apg1text = 'APG: {}'.format(apg1)
    #Creating stat canvas with appropriate attributes based on player generation
    stat1root = Tk()
    stat1Canvas = Canvas(stat1root, height = 800, width = 600, bg = stat1Bg)
    stat1Canvas.pack()
    stat1Header = stat1Canvas.create_text(250, 75, text = pOne, fill = 'white', font = (textFont, '18'),)
    stat1Pos = stat1Canvas.create_text(550, 75, text = pos1, fill = 'white', font = (textFont, '18'))
    stat1Star = stat1Canvas.create_text(300, 200, text = star1, fill = 'white', font = (textFont, '25'))
    stat1PPG = stat1Canvas.create_text(300, 350, text = ppg1text, fill = 'white', font = (textFont, '25'))
    stat1RPG = stat1Canvas.create_text(300, 500, text = rpg1text, fill = 'white', font = (textFont, '25'))
    stat1APG = stat1Canvas.create_text(300, 650, text = apg1text, fill = 'white', font = (textFont, '25'))
    stat1Canvas.mainloop()
#Determining appropriate file for button-image based on player generation
if pOne == 'Giannis Antetokounmpo':
    file = 'giannis.gif'
elif pOne == 'Lamelo Ball':
    file = 'melo.gif'
else:
    file = 'ja.gif'
#Removing file/player from main lists, appending to lists used in subsequent functions
pList.remove(pOne)
playerSelectList.append(pOne)
fileList.remove(file)
payFileList.append(file)
#Creating player button and header based on player generation
pOneHeader = draftScreen.create_text(250, 225, text = pOne, fill = 'white', font = (textFont, '15'))
pOneImage = PhotoImage(file = file)
pOneB = Button(root1, height = 525, width = 315, image = pOneImage, borderwidth = 0.5, cursor = 'target', command = pOneSelect)
pOneButton = draftScreen.create_window(250, 550, window = pOneB)
pOneStatB = Button(root1, text = 'Stats', cursor = 'target', command = statCommand)
pOneStatButton = draftScreen.create_window(250, 875, window = pOneStatB)
#Function for stat screen for second player in generated pool
def statCommand2():
    #Setting canvas attributes for each individual player upon generation
    if pTwo == 'Zion Williamson':
        stat2Bg = 'firebrick2'
        fill2 = 'white'
        pos2 = 'PF'
        star2 = '5 ★★★★★'
        ppg2 = 26.5
        rpg2 = 7.1
        apg2 = 3.6
    elif pTwo == 'Kawhi Leonard':
        stat2Bg = 'gray26'
        fill2 = 'white'
        pos2 = 'SF'
        star2 = '5 ★★★★★'
        ppg2 = 25.8
        rpg2 = 6.6
        apg2 = 5.0
    else:
        stat2Bg = 'gold'
        fill2 = 'grey50'
        pos2 = 'PG'
        star2 = '5 ★★★★★'
        ppg2 = 29.7
        rpg2 = 5.5
        apg2 = 6.0
    #Formatting stat text to include previously set variables
    ppg2text = 'PPG: {}'.format(ppg2)
    rpg2text = 'RPG: {}'.format(rpg2)
    apg2text = 'APG: {}'.format(apg2)
    #Creating stat canvas with appropriate attributes based on player generation
    stat2root = Tk()
    stat2Canvas = Canvas(stat2root, height = 800, width = 600, bg = stat2Bg)
    stat2Canvas.pack()
    stat2Header = stat2Canvas.create_text(250, 75, text = pTwo, fill = fill2, font = (textFont, '18'),)
    stat2Pos = stat2Canvas.create_text(550, 75, text = pos2, fill = fill2, font = (textFont, '18'))
    stat2Star = stat2Canvas.create_text(300, 200, text = star2, fill = fill2, font = (textFont, '25'))
    stat2PPG = stat2Canvas.create_text(300, 350, text = ppg2text, fill = fill2, font = (textFont, '25'))
    stat2RPG = stat2Canvas.create_text(300, 500, text = rpg2text, fill = fill2, font = (textFont, '25'))
    stat2APG = stat2Canvas.create_text(300, 650, text = apg2text, fill = fill2, font = (textFont, '25'))
    stat2Canvas.mainloop()
#Determining appropriate file for button-image based on player generation
if pTwo == 'Zion Williamson':
    file2 = 'zion.gif'
elif pTwo == 'Kawhi Leonard':
    file2 = 'kawhi.gif'
else:
    file2 = 'curry.gif'
#Removing file/player from main lists, appending to lists used in subsequent functions
pList.remove(pTwo)
playerSelectList.append(pTwo)
fileList.remove(file2)
payFileList.append(file2)
#Creating player button and header based on player generation
pTwoHeader = draftScreen.create_text(800, 225, text = pTwo, fill = 'white', font = (textFont, '15'))
pTwoBImage = PhotoImage(file = file2)
pTwoB = Button(root1, height = 525, width = 315, image = pTwoBImage, borderwidth = 0.5, cursor = 'target', command = pTwoSelect)
pTwoButton = draftScreen.create_window(800, 550, window = pTwoB)
pTwoStatB = Button(root1, text = 'Stats', cursor = 'target', command = statCommand2)
pTwoStatButton = draftScreen.create_window(800, 875, window = pTwoStatB)
#Function for stat screen for third player in generated pool
def statCommand3():
    #Setting canvas attributes for each individual player upon generation
    if pThree == 'Kevin Durant':
        stat3Bg = 'black'
        fill3 = 'white'
        pos3 = 'SF'
        star3 = '5 ★★★★★'
        ppg3 = 28.1
        rpg3 = 7.3
        apg3 = 5.2
    elif pThree == 'Anthony Edwards':
        stat3Bg = 'green yellow'
        fill3 = 'navy'
        pos3 = 'SG'
        star3 = '4 ★★★★'
        ppg3 = 17.9
        rpg3 = 4.4
        apg3 = 2.6
    elif pThree == 'Lebron James':
        stat3Bg = 'purple4'
        fill3 = 'gold'
        pos3 = 'SF'
        star3 = '5 ★★★★★'
        ppg3 = 25.4
        rpg3 = 7.9
        apg3 = 7.9
    #Formatting stat text to include previously set variables
    ppg3text = 'PPG: {}'.format(ppg3)
    rpg3text = 'RPG: {}'.format(rpg3)
    apg3text = 'APG: {}'.format(apg3)
    #Creating stat canvas with appropriate attributes based on player generation
    stat3root = Tk()
    stat3Canvas = Canvas(stat3root, height = 800, width = 600, bg = stat3Bg)
    stat3Canvas.pack()
    stat3Header = stat3Canvas.create_text(250, 75, text = pThree, fill = fill3, font = (textFont, '18'),)
    stat3Pos = stat3Canvas.create_text(550, 75, text = pos3, fill = fill3, font = (textFont, '18'))
    stat3Star = stat3Canvas.create_text(300, 200, text = star3, fill = fill3, font = (textFont, '25'))
    stat3PPG = stat3Canvas.create_text(300, 350, text = ppg3text, fill = fill3, font = (textFont, '25'))
    stat3RPG = stat3Canvas.create_text(300, 500, text = rpg3text, fill = fill3, font = (textFont, '25'))
    stat3APG = stat3Canvas.create_text(300, 650, text = apg3text, fill = fill3, font = (textFont, '25'))
    stat3Canvas.mainloop()
#Determining appropriate file for button-image based on player generation 
if pThree == 'Lebron James':
    file3 = 'bron.gif'
elif pThree == 'Kevin Durant':
    file3 = 'kd.gif'
else:
    file3 = 'ant.gif' 
#Removing file/player from main lists, appending to lists used in subsequent functions
pList.remove(pThree)
playerSelectList.append(pThree)
fileList.remove(file3)
payFileList.append(file3)
#Creating player button and header based on player generation
pThreeHeader = draftScreen.create_text(1350, 225, text = pThree, fill = 'white', font = (textFont, '15'))
pThreeBImage = PhotoImage(file = file3)
pThreeB = Button(root1, height = 525, width = 315, image = pThreeBImage, borderwidth = 0.5, cursor = 'target', command = pThreeSelect)
pThreeButton = draftScreen.create_window(1350, 550, window = pThreeB)
pThreeStatB = Button(root1, text = 'Stats', cursor = 'target', command = statCommand3)
pThreeStatButton = draftScreen.create_window(1350, 875, window = pThreeStatB)

draftScreen.mainloop()

#----------------------------------------------------------------------
#Creating trade screen canvas
root2 = Tk()
tradeScreen = Canvas(root2, height = canvasHeight, width = canvasWidth)
tradeScreen.pack()
#Configuring cursor
root2.config(cursor = 'circle')
#Setting background image
tradeBgImage = PhotoImage(file = 'tradebg.gif')
tradeBg = tradeScreen.create_image(bgImageA, bgImageB, image = tradeBgImage)
#Function to reveal elements of trade screen once the "view" button is activated by changing element state
def reveal():
    tradeScreen.itemconfig(incomingHeader, state = HIDDEN)
    tradeScreen.itemconfig(viewButton, state = HIDDEN)
    tradeScreen.itemconfig(tradeHeader1, state = NORMAL)
    tradeScreen.itemconfig(tradeHeader2, state = NORMAL)
    tradeScreen.itemconfig(tradePImage, state = NORMAL)
    tradeScreen.itemconfig(tradeStatButton, state = NORMAL)
    tradeScreen.itemconfig(acceptButton, state = NORMAL)
    tradeScreen.itemconfig(declineButton, state = NORMAL)
    tradeScreen.itemconfig(choseSong, state = NORMAL)
    tradeScreen.itemconfig(drakeButton, state = NORMAL)
    tradeScreen.itemconfig(tjayButton, state = NORMAL)
    tradeScreen.itemconfig(roddyButton, state = NORMAL)
    tradeScreen.itemconfig(babyButton, state = NORMAL)
#Series of functions for array of song choices while in trade screen
def drake():
    mixer.music.stop()
    drakeList = ['toosie.mp3', 'laugh cry.mp3', 'life good.mp3']
    drakeSong = random.choice(drakeList)
    mixer.music.load(drakeSong)
    mixer.music.set_volume(100)
    mixer.music.play()
def tjay():
    mixer.music.stop()
    tjayList = ['fn.mp3', 'call.mp3', 'mood.mp3']
    tjaySong = random.choice(tjayList)
    mixer.music.load(tjaySong)
    mixer.music.set_volume(100)
    mixer.music.play()
def roddy():
    mixer.music.stop()
    rodList = ['ball.mp3', 'box.mp3', 'rock.mp3']
    rodSong = random.choice(rodList)
    mixer.music.load(rodSong)
    mixer.music.set_volume(100)
    mixer.music.play()
def baby():
    mixer.music.stop()
    babyList = ['drip.mp3', 'big.mp3', 'on.mp3']
    babySong = random.choice(babyList)
    mixer.music.load(babySong)
    mixer.music.set_volume(100)
    mixer.music.play()
#Header/buttons for individual artists in previous functions
choseSong = tradeScreen.create_text(200, 900, text = 'Listen To One Of The Following Artists While Deciding', fill = 'white', font = (textFont, '7'), state = HIDDEN)
drakeB = Button(root2, width = 10, height = 2, text = 'Drake', cursor = 'target', command = drake)
drakeButton = tradeScreen.create_window(115, 960, window = drakeB, state = HIDDEN)
tjayB = Button(root2, width = 10, height = 2, text = 'Lil Tjay', cursor = 'target', command = tjay)
tjayButton = tradeScreen.create_window(280, 960, window = tjayB, state = HIDDEN)
roddyB = Button(root2, width = 10, height = 2, text = 'Roddy', cursor = 'target', command = roddy)
roddyButton = tradeScreen.create_window(115, 1050, window = roddyB, state = HIDDEN)
babyB = Button(root2, width = 10, height = 2, text = 'Lil Baby', cursor = 'target', command = baby)
babyButton = tradeScreen.create_window(280, 1050, window = babyB, state = HIDDEN)
#Header/view button for trade screen (PT1)
incomingHeader = tradeScreen.create_text(825, 410, text = 'You Have An Incoming Trade Request. Click "View" To View', fill = 'white', font = (textFont, '25'))
viewB = Button(root2, width = 10, height = 2, text = 'View', cursor = 'target', command = reveal)
viewButton = tradeScreen.create_window(825, 550, window = viewB)
#Randomly generating player/file to be used in the trade 
randomPNum = random.randint(0, 5)
randomP = pList[randomPNum]
randomPFile = fileList[randomPNum]
#Altering previously set variables to randomly-generated player; to be used in previously set stat functions
pOne = randomP
pTwo = randomP
pThree = randomP
#Determining which list the randomly-generated player exists in to use appropriate stat function
def tradeStat():
    if randomP in pOneList:
        statCommand()
    elif randomP in pTwoList: 
        statCommand2()
    elif randomP in pThreeList:
        statCommand3()
#Creating header by formatting variables; creating player and stat buttons (PT2)   
tradeTeam = random.choice(teamsList)
tradeText1 = 'The {} Are Offering'.format(tradeTeam)
tradeText2 = '{} For'.format(randomP)
tradeText3 = pSelect[0]
tradeHeaderText2 = tradeText2 + ' ' + tradeText3
tradeHeader1 = tradeScreen.create_text(825, 100, text = tradeText1, fill = 'white', font = (textFont, '27'), state = HIDDEN)
tradeHeader2 = tradeScreen.create_text(825, 175, text = tradeHeaderText2, fill = 'white', font = (textFont, '27'), state = HIDDEN)
tradeImage = PhotoImage(file = randomPFile)
tradePImage = tradeScreen.create_image(825, 550, image = tradeImage, state = HIDDEN)
tradeStatB = Button(root2, text = 'Stats', cursor = 'target', command = tradeStat)
tradeStatButton = tradeScreen.create_window(825, 900, window = tradeStatB, state = HIDDEN)
#Function for if the trade is accepted (appends randomP to selected list (pSelect))
def accept():
    global payFile 
    mixer.music.stop()
    pSelect.pop(0)
    pSelect.append(randomP)
    payFile = randomPFile
    root2.destroy()
#Function for if the trade is declined (retains the same player for pSelect[0])
def decline():
    global payFile
    mixer.music.stop()
    for i in range (0, 3):
        if pSelect[0] == playerSelectList[i]:
            payFile = payFileList[i]
    root2.destroy() 
#Creating accept/decline buttons
acceptB = Button(root2, width = 10, height = 2, text = 'Accept', cursor = 'target', command = accept)
acceptButton = tradeScreen.create_window(1375, 1050, window = acceptB, state = HIDDEN)
declineB = Button(root2, width = 10, height = 2, text = 'Decline', cursor = 'target', command = decline)
declineButton = tradeScreen.create_window(1550, 1050, window = declineB, state = HIDDEN)

root2.mainloop()

#--------------------------------------------------------------------
#Function for proceeding to next screen
def nxt():
    mixer.music.stop()
    root3.destroy()
#Creating canavs for negotiation screen
root3 = Tk()
payScreen = Canvas(root3, height = canvasHeight, width = canvasWidth)
payScreen.pack()
#Configuring cursor
root3.config(cursor = 'plus')
#Playing audio using pygame mixer
mixer.music.load("ybn.mp3")
mixer.music.set_volume(100)
mixer.music.play()
#Setting background image
payBgImage = PhotoImage(file = 'paybg.gif')
payBg = payScreen.create_image(bgImageA, bgImageB, image = payBgImage)
#Setting player image/header for negotiation
payPImage = PhotoImage(file = payFile)
payPlayerImage = payScreen.create_image(375, 500, image = payPImage)
payName = pSelect[0]
payHeader = payScreen.create_text(375, 150, text = payName, fill = 'white', font = (textFont, '25'))
#Creating labels to indicate salary range and restrictions (min/max)
payMin = payScreen.create_text(375, 850, text = 'Minimum Contract - $500k, 1-year', fill = 'red', font = (textFont, '18'))
payMax = payScreen.create_text(375, 950, text = 'Maximum Contract - $75M, 1-year', fill = 'green', font = (textFont, '18'))
#Spinbox for user to enter proposed base-salary value from a range of values (set by salary restrictions) (FUNCTION 2/2)
salHeader =  payScreen.create_text(1125, 300, text = 'Base Salary (USD)', fill = 'white', font = (textFont, '18'))
salSpin = Spinbox(root3, from_=500000, to = 75000000, increment = 5000000)
salSpinBox = payScreen.create_window(1450, 300, window = salSpin)
#Spinbox for user to enter period (years) of proposed contract (FUNCTION 2/2)
yearHeader =  payScreen.create_text(1090, 450, text = 'Contract Period (Years)', fill = 'white', font = (textFont, '18'))
yearSpin = Spinbox(root3, from_=1, to = 10, increment = 1) 
yearSpinBox = payScreen.create_window(1450, 450, window = yearSpin)
#Function using probability to simulate negotiation
def offer(): 
    global sal, year
    #Reciving input from spinboxes
    sal = int(salSpin.get())
    year = int(yearSpin.get())
    #Setting choice to False, will be altered to True if the contract is accepted
    choice = False
    high = pSelect[0] + ' is Asking For A Higher Contract'
    highHeader = payScreen.create_text(1250, 700, text = high, fill = 'white', font = (textFont, '15'), state = HIDDEN)
    #The probability of acceptance increases with each incremental increase in salary
    if sal <= 25000000:
        lowSal = random.randint(1, 100)
        if lowSal <= 20:
            choice = True
    elif sal <= 50000000:
        medSal = random.randint(1, 100)
        if medSal <= 50:
            choice = True
    elif sal <= 75000000:
        hiSal = random.randint(1, 100)
        if hiSal <= 80:
            choice = True
    if choice == False:
        payScreen.itemconfig(highHeader, state = NORMAL)
    elif choice == True:
        payScreen.itemconfig(proceedButton2, state = NORMAL)
#Creating buttons for proposal/proceeding to next screen
proposeB = Button(root3, text = "Propose", width = 10, height = 2, command = offer)
proposeButton = payScreen.create_window(1250, 600, window = proposeB)
proceedB2 = Button(root3, width = 10, height = 2, text = 'Proceed', cursor = 'target', command = nxt)
proceedButton2 = payScreen.create_window(1590, 1060, window = proceedB2, state = HIDDEN)

root3.mainloop() 

#--------------------------------------------------------------------
#Function to end canvas once corresponding button is pressed
def end():
    root4.destroy()
    mixer.music.stop()
#Creating canvas for final screen
root4 = Tk()
confScreen = Canvas(root4, height = canvasHeight, width = canvasWidth)
confScreen.pack()
#Configuring cursor
root4.config(cursor = 'circle')
#Playing audio using pygame mixer
mixer.music.load("end.mp3")
mixer.music.set_volume(100)
mixer.music.play(-1)
#Setting background image
confBgImage = PhotoImage(file = 'confbg.gif')
confBg = confScreen.create_image(bgImageA, bgImageB, image = confBgImage)
#Creating header outlining contract by formating multiple varibales (selected team, contract total, period)
confText1 = 'Congratulations, The {} Have Signed '.format(playerTeam) + pSelect[0]
contTotal = sal*year
confText2 = 'For ${}'.format(contTotal) + ' Over A {}-Year Period'.format(year)
confHeader1 = confScreen.create_text(825, 100, text = confText1, fill = 'white', font = (textFont, '22'))
confHeader2 = confScreen.create_text(825, 175, text = confText2, fill = 'white', font = (textFont, '22'))
#Creating image to display selected player
confPImage = PhotoImage(file = payFile)
confPlayerImage = confScreen.create_image(825, 575, image = confPImage)
#Creating button to end program
endB = Button(root4, text = 'End', width = 10, height = 2, cursor = 'target', command = end)
endButton = confScreen.create_window(1590, 1060, window = endB)

root4.mainloop()
