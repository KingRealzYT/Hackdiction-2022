from cmu_graphics import *

# Keybinds, Exit and Back system from https://github.com/KingRealzYT/Runner

# Start screen Variables
app.startScreen = True
app.keybindsScreen = False
app.infoScreen = False
app.levelScreen = False

# Score Variables
app.score = 0
score = Label('Score: ' + str(app.score), 350, 60, fill='white', visible=False)

# Menu Variables
app.menuOn = False

# World Variables
app.world1a1 = False
app.world1a2 = False
app.levelSelected = 'None'
app.levelPlay = False

# Health Variables
app.health = 0

# Level Variables
app.l1 = False

# Level 1 Variables
level1Group = Group()
l1b1 = Rect(0, 280, 400, 120, fill='green', visible=False)
l1b2 = Arc(0, 0, 80, 100, 0, 180, fill='yellow', visible=False)
l1h1 = Circle(320, 20, 10, fill='black', visible=False)
l1h2 = Circle(350, 20, 10, fill='black', visible=False)
l1h3 = Circle(380, 20, 10, fill='black', visible=False)
l1h4 = Label('Health: ' + str(app.health), 350, 40, fill='white', visible=True)

level1Group.add(l1b1, l1b2, l1h1, l1h2, l1h3, l1h4, score)

level1Group.visible = False

# Level 1 Death Zones
DeathZone1 = Group()
dz1 = Rect(-400, 0, 425, 25, fill='red', opacity=25)
dz2 = Rect(100, 0, 400, 25, fill='red', opacity=25)
DeathZone1.add(dz1, dz2)
DeathZone1.speed = 6
DeathZone1.visible = False

# Keybinds Variables
app.changeLeftKeybind = False
app.changeRightKeybind = False
app.leftKeybind = 'a'
app.rightKeybind = 'd'
app.menuKeybind = 'escape'

# Exit and Backbutton Variables
app.confirmExit = False
app.backButtonEnabled = False

# Background
app.background = 'black'

# Back Button
backLabel = Label('Back!', 40, 20, fill='white', size=25, visible=False)
backLabelHitbox = Rect(0, 0, 80, 40, fill=None, border='white', borderWidth=2, visible=False)

# Start Screen Labels
startScreenLabels = Group()
gameName = Label('Contra', 200, 40, fill='white', size=25)
gameStart = Label('Start', 200, 150, fill='white', size=25)
gameKeybinds = Label('Keybinds', 60, 225, fill='white', size=25)
gameInfo = Label('Information', 330, 225, fill='white', size=25)
gameMenuInstruction = Label('Use your mouse and click a label', 200, 360, fill='white', size=25)
gameExit = Label('Exit', 370, 20, fill='white', size=25)
startScreenLabels.add(gameName, gameStart, gameKeybinds, gameInfo, gameMenuInstruction, gameExit)

# Level Selector
lsGroup = Group()
ls1 = Rect(120, 40, 160, 120, fill=None, border='white', borderWidth=2)
ls2 = Label('Level Selected: ' + app.levelSelected, 200, 60, fill='white', size=20)
ls3 = Label('Play!', 200, 140, size=20, fill='white', visible=False)
ls4 = Rect(160, 120, 80, 40, fill=None, border='white', borderWidth=1, visible=False)
lsGroup.add(ls1, ls2)

lsGroup.visible = False

# World 1 Area 1 Labels and Shapes
w1a1Group = Group()
w1a1s = Arc(0, 0, 80, 100, 0, 180, fill='yellow', visible=False)
w1a1g = Rect(0, 280, 400, 120, fill='green')
w1a1l11 = Rect(60, 240, 10, 40, fill='white')
w1a1l12 = Rect(50, 239, 10, 15, fill='white', rotateAngle=20)
w1a1l13 = Rect(55, 238, 15, 10, fill='white')
w1a1l14 = Rect(50, 270, 30, 10, fill='white')
w1a1l1 = Line(280, 240, 360, 240, fill='white', arrowEnd=True)
w1a1l2 = Label('Bring your player past the right wall!', 200, 320, fill='white', size=25, visible=False)
w1a1l3 = Label('Use your mouse to select a level!', 200, 200, fill='white', size=25, visible=False)
w1a1l15 = Rect(45, 235, 37, 45, fill='green', opacity=35, visible=False)
w1a1Group.add(w1a1s, w1a1g, w1a1l11, w1a1l12, w1a1l13, w1a1l14, w1a1l1, w1a1l2, w1a1l3)

w1a1Group.visible = False

# World 1 Area 2 Labels and Shapes
w1a2Group = Group()
w1a2g = Rect(0, 280, 400, 120, fill='green', visible=False)
w1a2l1 = Line(120, 240, 280, 240, fill='white', arrowStart=True, visible=False)
w1a2Closed = Label('This area is still in Progress! Come back later!', 200, 200, fill='white', size=15, visible=False)
w1a2Group.add(w1a2g, w1a2l1, w1a2Closed)

w1a2Group.visible = False

# Menu
menu = Group()
menu1 = Rect(120, 80, 160, 160, fill='white', visible=False)
menu2 = Rect(120, 80, 160, 160, fill=None, border='black', borderWidth=4, visible=False)
menu3 = Label('Menu', 200, 100, fill='black', size=25, visible=False)
menu4 = Label('Home', 200, 220, fill='black', size=25, visible=False)
menu5 = Label('Exit', 200, 160, fill='black', size=25, visible=False)
menu6 = Rect(160, 205, 80, 30, fill=None, border='black', borderWidth=2, visible=False)
menu7 = Rect(175, 145, 50, 30, fill=None, border='black', borderWidth=2, visible=False)
menu.add(menu1, menu2, menu3, menu4, menu5, menu6, menu7)

menu.visible = False

shuffleKeybinds = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

# Start Screen Hitboxes
startScreenHB = Group()
gameNameHB = Rect(155, 20, 90, 40, fill='white', opacity=25, visible=False)
gameStartHB = Rect(170, 135, 60, 30, fill='white', opacity=25, visible=False)
gameKeybindsHB = Rect(5, 210, 110, 30, fill='white', opacity=25, visible=False)
gameInfoHB = Rect(265, 210, 130, 30, fill='white', opacity=25, visible=False)
gameExitHB = Rect(345, 5, 50, 30, fill=None, border='white', borderWidth=2, visible=False)
startScreenHB.add(gameNameHB, gameStartHB, gameKeybindsHB, gameInfoHB, gameExitHB)
startScreenHB.visible = False

# Exit Game Menu
exitConfGroup = Group()
exitConf1 = Rect(170, 220, 60, 70, fill=None, border='white', borderWidth=2, visible=False)
exitConf2 = Label('Yes', 200, 240, fill='white', size=25, visible=False)
exitConf3 = Label('No', 200, 270, fill='white', size=25, visible=False)
exitConf4 = Rect(170, 220, 60, 36, fill='white', opacity=25, visible=False)
exitConf5 = Rect(170, 256, 60, 30, fill='white', opacity=25, visible=False)
exitConfGroup.add(exitConf1, exitConf2, exitConf3, exitConf4, exitConf5)

exitConfGroup.visible = False

# Keybinds Screen Labels
keybindsScreenLabels = Group()
keybindsLabel = Label('Keybinds', 200, 20, fill='white', size=25)
leftKeybindsLabel = Label('Left: ' + app.leftKeybind, 40, 80, fill='white', size=25, visible=False)
rightKeybindsLabel = Label('Right: ' + app.rightKeybind, 47, 120, fill='white', size=25, visible=False)
menuKeybindsLabel = Label('Menu: ' + app.menuKeybind, 85, 165, fill='white', size=25, visible=False)
howToKeybindsLabel = Label('Click the keybind then a letter to change it!', 200, 200, fill='white', size=20,
                           visible=False)
randomizeKeybindsLabel = Label('Randomize!', 200, 320, fill='white', size=25)
resetKeybindsLabel = Label('Reset Keybinds!', 100, 370, fill='white', size=25)
keybindsScreenLabels.add(keybindsLabel, leftKeybindsLabel, rightKeybindsLabel, menuKeybindsLabel, howToKeybindsLabel,
                         randomizeKeybindsLabel, resetKeybindsLabel)
keybindsScreenLabels.visible = False

# Keybinds Screen Hitbox
leftKeybindsHB = Rect(3, 65, 75, 30, fill='white', opacity=25, visible=False)
rightKeybindsHB = Rect(3, 105, 90, 30, fill='white', opacity=25, visible=False)
randomizeKeybindsHB = Rect(130, 300, 140, 40, fill=None, border='white', borderWidth=2, visible=False)
resetKeybindsHB = Rect(3, 350, 195, 40, fill=None, border='white', borderWidth=2, visible=False)

# Choose a Keybind Screen
cks2 = Label('', 200, 280, fill='white', size=25, visible=False)

# Information Screen Labels
infoGroup = Group()
infoTitle = Label('Information!', 200, 20, fill='white', size=25, visible=False)
info1 = Label('This game is Contra!', 200, 160, fill='white', size=25, visible=False)
info2 = Label('You have 3 lives', 200, 200, fill='white', size=25, visible=False)
info3 = Label("But everything isn't as it seems", 200, 240, fill='white', size=25, visible=False)
infoGroup.add(infoTitle, info1, info2, info3)

infoGroup.visible = False

# Player Variables and Shapes
app.playerMovement = False
player = Rect(0, 260, 20, 20, fill='red', visible=False)
player.toFront()


# Back Function
def goBack():
    if not app.changeLeftKeybind:
        if not app.changeRightKeybind:
            if app.backButtonEnabled:
                startScreenLabels.visible = True
                keybindsScreenLabels.visible = False
                infoGroup.visible = False
                app.startScreen = True
                app.keybindsScreen = False
                app.infoScreen = False
                backLabel.visible = False
                backLabelHitbox.visible = False
                app.backButtonEnabled = False
                app.l1 = False
                level1Group.visible = False
    if app.changeLeftKeybind or app.changeRightKeybind:
        print('debug')
        cks2.value = "Choose a Keybind First!"


# Level 1 Function
def level1():
    app.background = 'skyBlue'
    level1Group.visible = True
    app.l1 = True
    app.world1a1 = False
    app.world1a2 = False
    w1a1Group.visible = False
    w1a2Group.visible = False
    lsGroup.visible = False
    ls3.visible = False
    ls4.visible = False
    w1a1l15.visible = False
    DeathZone1.visible = True
    score.visible = True


def nextDZ1():
    DeathZone1.bottom = 0
    DeathZone1.centerX = randrange(50, 350)


# Move Death Zone 1
def moveDz1():
    if app.l1:
        DeathZone1.top += DeathZone1.speed
        if DeathZone1.top >= 400:
            app.score += 1
            score.value = 'Score: ' + str(app.score)

            if DeathZone1.speed < 11:
                DeathZone1.speed += 1

            nextDZ1()


def winGame():
    app.l1 = False
    level1Group.visible = False
    player.visible = False
    app.background = 'black'


# End Game Function
def endGame():
    app.l1 = False
    level1Group.visible = False
    player.visible = False
    app.background = 'black'


# Check whenever the mouse Moves
def onMouseMove(x, y):
    # Highlight start screen hitboxes
    if app.startScreen:
        if gameNameHB.contains(x, y):
            gameNameHB.visible = True
        else:
            gameNameHB.visible = False

        if gameStartHB.contains(x, y):
            gameStartHB.visible = True
        else:
            gameStartHB.visible = False

        if gameKeybindsHB.contains(x, y):
            gameKeybindsHB.visible = True
        else:
            gameKeybindsHB.visible = False

        if gameInfoHB.contains(x, y):
            gameInfoHB.visible = True
        else:
            gameInfoHB.visible = False

        if gameExitHB.contains(x, y):
            gameExitHB.visible = True
        else:
            gameExitHB.visible = False

    if app.keybindsScreen:
        if leftKeybindsHB.contains(x, y):
            leftKeybindsHB.visible = True
        else:
            leftKeybindsHB.visible = False
        if rightKeybindsHB.contains(x, y):
            rightKeybindsHB.visible = True
        else:
            rightKeybindsHB.visible = False
        if randomizeKeybindsHB.contains(x, y):
            randomizeKeybindsHB.visible = True
        else:
            randomizeKeybindsHB.visible = False
        if resetKeybindsHB.contains(x, y):
            resetKeybindsHB.visible = True
        else:
            resetKeybindsHB.visible = False

    # Exit hitbox
    if app.confirmExit:
        if exitConf4.contains(x, y):
            exitConf4.visible = True
        else:
            exitConf4.visible = False

        if exitConf5.contains(x, y):
            exitConf5.visible = True
        else:
            exitConf5.visible = False

    # Backbutton
    if app.backButtonEnabled:
        if backLabelHitbox.contains(x, y):
            backLabelHitbox.visible = True
        else:
            backLabelHitbox.visible = False


# Check whenever the mouse is pressed
def onMousePress(x, y):
    if app.menuOn:
        if menu6.contains(x, y):
            w1a1Group.visible = False
            app.playerMovement = False
            player.left = 0
            app.background = 'black'
            app.world1a1 = False
            app.startScreen = True
            player.visible = False
            menu.visible = False
            lsGroup.visible = False
            w1a1l15.visible = False
            ls3.visible = False
            ls4.visible = False
            app.menuOn = False
            app.levelSelected = 'None'
            ls2.value = 'Level Selected: ' + app.levelSelected
            app.backButtonEnabled = True
            goBack()
        if menu7.contains(x, y):
            app.confirmExit = True
            exitConfGroup.visible = True
            exitConfGroup.centerY = 270

        if gameExitHB.contains(x, y):
            app.confirmExit = True
            exitConfGroup.visible = True
            exitConf4.visible = False
            exitConf5.visible = False
        if app.confirmExit:
            if exitConf4.contains(x, y):
                exit()
            elif exitConf5.contains(x, y):
                exitConfGroup.centerY = 250
                exitConfGroup.visible = False
                app.confirmExit = False
    if app.startScreen:
        # Switch to World 1
        if gameStartHB.contains(x, y):
            app.startScreen = False
            app.world1a1 = True
            startScreenLabels.visible = False
            gameStartHB.visible = False
            app.background = 'skyBlue'
            w1a1Group.visible = True
            app.playerMovement = True
            ls3.visible = False
            ls4.visible = False
            w1a1l15.visible = False
        # Switch to Keybinds Screen
        if gameKeybindsHB.contains(x, y):
            app.startScreen = False
            app.keybindsScreen = True
            startScreenLabels.visible = False
            keybindsScreenLabels.visible = True
            gameKeybindsHB.visible = False
            app.backButtonEnabled = True
            backLabel.visible = True

        # Switch to Information Screen
        if gameInfoHB.contains(x, y):
            app.startScreen = False
            app.infoScreen = True
            startScreenLabels.visible = False
            gameInfoHB.visible = False
            app.backButtonEnabled = True
            backLabel.visible = True
            infoGroup.visible = True

    # Level 1
    if app.world1a1:
        if w1a1l15.contains(x, y):
            if w1a1l15.visible:
                w1a1l15.visible = False
                ls2.size = 15
                app.levelSelected = 'None'
                ls2.value = 'Level Selected: ' + app.levelSelected
            else:
                w1a1l15.visible = True
                ls2.size = 20
                app.levelSelected = '1'
                ls2.value = 'Level Selected: ' + app.levelSelected
        if ls4.visible:
            if ls4.contains(x, y):
                app.l1 = True
                level1()

    # Exit Game Function
    if app.startScreen:
        if gameExitHB.contains(x, y):
            app.confirmExit = True
            exitConfGroup.visible = True
            exitConf4.visible = False
            exitConf5.visible = False
        if app.confirmExit:
            if exitConf4.contains(x, y):
                exit()
            elif exitConf5.contains(x, y):
                exitConfGroup.visible = False
                app.confirmExit = False

    # Go Back to Start Screen
    if app.backButtonEnabled:
        if backLabelHitbox.contains(x, y):
            goBack()
    # Change keybind if they click on it
    if app.keybindsScreen:
        if resetKeybindsHB.contains(x, y):
            app.leftKeybind = 'a'
            app.rightKeybind = 'd'
            leftKeybindsLabel.value = 'Left: ' + app.leftKeybind
            rightKeybindsLabel.value = 'Right: ' + app.rightKeybind
        if not app.changeLeftKeybind:
            if not app.changeRightKeybind:
                if randomizeKeybindsHB.contains(x, y):
                    app.leftKeybind = choice(shuffleKeybinds)
                    app.rightKeybind = choice(shuffleKeybinds)
                    leftKeybindsLabel.value = 'Left: ' + app.leftKeybind
                    rightKeybindsLabel.value = 'Right: ' + app.rightKeybind

                    if app.leftKeybind == 'space':
                        leftKeybindsLabel.centerX = 65
                        leftKeybindsHB.width = 125
                    elif app.leftKeybind == 'escape':
                        leftKeybindsLabel.centerX = 70
                        leftKeybindsHB.width = 130
                    else:
                        leftKeybindsLabel.centerX = 40
                        leftKeybindsHB.width = 75

                    if app.rightKeybind == 'space':
                        rightKeybindsLabel.centerX = 80
                        rightKeybindsHB.width = 150
                    elif app.rightKeybind == 'escape':
                        rightKeybindsLabel.centerX = 80
                        rightKeybindsHB.width = 150
                    else:
                        rightKeybindsLabel.centerX = 47
                        rightKeybindsHB.width = 90

                    if app.leftKeybind == app.rightKeybind or app.leftKeybind == app.menuKeybind:
                        app.leftKeybind = choice(shuffleKeybinds)
                        leftKeybindsLabel.value = 'Left: ' + app.leftKeybind
                    if app.rightKeybind == app.leftKeybind or app.leftKeybind == app.menuKeybind:
                        app.rightKeybind = choice(shuffleKeybinds)
                        rightKeybindsLabel.value = 'Right: ' + app.rightKeybind
        if leftKeybindsHB.contains(x, y):
            if not app.changeRightKeybind:
                if app.changeLeftKeybind:
                    app.changeLeftKeybind = False
                    cks2.visible = False
                else:
                    app.changeLeftKeybind = True
                    cks2.visible = True
                    cks2.value = 'Now Editing Left Keybind'
        elif rightKeybindsHB.contains(x, y):
            if not app.changeLeftKeybind:
                if app.changeRightKeybind:
                    app.changeRightKeybind = False
                    cks2.visible = False
                else:
                    app.changeRightKeybind = True
                    cks2.visible = True
                    cks2.value = 'Now Editing Right Keybind'


# Runs whenever a key is pressed
def onKeyPress(key):
    if key == app.menuKeybind:
        if not app.startScreen:
            if not app.keybindsScreen:
                if not app.infoScreen:
                    if menu.visible:
                        app.menuOn = False
                    else:
                        app.menuOn = True
    if app.keybindsScreen:
        # Change left Keybind
        if app.changeLeftKeybind:
            if key == app.leftKeybind or key == app.rightKeybind or key == app.menuKeybind:
                cks2.value = "Can't use that keybind!"
            else:
                app.leftKeybind = key
                leftKeybindsLabel.value = 'Left: ' + app.leftKeybind
                app.changeLeftKeybind = False
                cks2.visible = False
        # Check if the key is space
        if app.leftKeybind == 'space':
            leftKeybindsLabel.centerX = 65
            leftKeybindsHB.width = 125
        elif app.leftKeybind == 'escape':
            leftKeybindsLabel.centerX = 70
            leftKeybindsHB.width = 130
        else:
            leftKeybindsLabel.centerX = 40
            leftKeybindsHB.width = 75
        # Change right Keybind
        if app.changeRightKeybind:
            if key == app.leftKeybind or key == app.rightKeybind or key == app.menuKeybind:
                cks2.value = "Can't use that keybind!"
            else:
                app.rightKeybind = key
                rightKeybindsLabel.value = 'Right: ' + app.rightKeybind
                app.changeRightKeybind = False
                cks2.visible = False
        if app.rightKeybind == 'space':
            rightKeybindsLabel.centerX = 75
            rightKeybindsHB.width = 145
        elif app.rightKeybind == 'escape':
            rightKeybindsLabel.centerX = 80
            rightKeybindsHB.width = 150
        else:
            rightKeybindsLabel.centerX = 47
            rightKeybindsHB.width = 90
        # Change Menu Keybind
        if app.menuKeybind == 'escape':
            menuKeybindsLabel.centerX = 85


# Runs when a key is being held
def onKeyHold(keys):
    if app.playerMovement:
        if app.leftKeybind in keys:
            if app.playerMovement:
                player.centerX -= 5
        elif app.rightKeybind in keys:
            if app.playerMovement:
                player.centerX += 5
        if app.l1:
            if app.leftKeybind in keys:
                if app.playerMovement:
                    player.centerX -= 10
            elif app.rightKeybind in keys:
                if app.playerMovement:
                    player.centerX += 10


# Runs every second
def onStep():
    if app.l1:
        moveDz1()
        if player.hitsShape(dz1) or player.hitsShape(dz2):
            nextDZ1()
            app.health += randrange(15, 25)
            l1h4.value = 'Health: ' + str(app.health)
        if app.health >= 33:
            l1h1.fill = rgb(0, 255, 0)
        if app.health >= 67:
            l1h2.fill = rgb(0, 255, 0)
        if app.health >= 100:
            l1h3.fill = rgb(0, 255, 0)
        if player.left < 0:
            player.left = 0
        elif player.right > 400:
            player.right = 400
        if app.health >= 100:
            endGame()
        if app.score >= 20:
            winGame()
    if app.menuOn:
        menu.visible = True
        app.playerMovement = False
    else:
        menu.visible = False
        app.playerMovement = True
    if app.world1a1:
        if player.left < 0:
            player.left = 0
        elif player.right > 400:
            app.world1a1 = False
            app.world1a2 = True
            player.left = 0
            lsGroup.visible = False
            ls3.visible = False
            ls4.visible = False
            w1a1l15.visible = False
    elif app.world1a2:
        if player.left < 0:
            app.world1a1 = True
            app.world1a2 = False
            player.right = 400
            app.levelSelected = 'None'
            ls2.value = 'Level Selected: ' + app.levelSelected
        elif player.right > 400:
            player.right = 400
    if app.world1a1:
        w1a1Group.visible = True
        player.visible = True
        w1a2Group.visible = False
        lsGroup.visible = True
        if app.levelSelected == 'None':
            ls2.size = 15
            ls3.visible = False
            ls4.visible = False
            app.levelPlay = False
        else:
            ls3.visible = True
            ls4.visible = True
            app.levelPlay = True
    if app.world1a2:
        w1a1Group.visible = False
        w1a2Group.visible = True
        lsGroup.visible = False


cmu_graphics.run()
