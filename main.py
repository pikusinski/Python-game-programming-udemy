import sys
import random

class Main:

   maxWidth = 5
   maxHeight = 5

   characterAlive = False
   characterWon = False

   monsterAwake = True
   monsterAwakened = False
   monsterMovePerTurn = 2

   def __init__(self):
      self.displayMenu()
      self.resetCurrentGame()

   def placeCharacter(self):
      
      self.characterPosition = [0,0]

   def resetCurrentGame(self):
      self.characterPosition = [0,0]
      self.monsterPosition = [1,0]
      self.trapPosition = [2,0]
      self.flaskPosition = [1,0]

   def resetAllSettings(self):
      self.characterAlive = True
      self.monsterAwake = False
      self.characterWon = False
      self.monsterAwakened = False

   def placeMonster(self):
      
      self.monsterPosition = [random.randint(0, self.maxWidth - 1), random.randint(0, self.maxHeight - 1)]
      if(self.coordinateCollision("monster", "player")):
         self.placeMonster()
      elif(self.coordinateCollision("monster", "flask")):
         self.placeMonster()
      elif(self.coordinateCollision("monster", "trap")):
         self.placeMonster()
      else:
         return True
      return True

   def placeTrap(self):
      
      self.trapPosition = [random.randint(0, self.maxWidth -1), random.randint(0, self.maxHeight - 1)]
      if(self.coordinateCollision("trap", "player")):
         self.placeTrap()
      elif(self.coordinateCollision("trap", "flask")):
         self.placeTrap()
      elif(self.coordinateCollision("trap", "monster")):
         self.placeTrap()
      else:
         return True
      return True

   def placeFlask(self):
      
      self.flaskPosition = [random.randint(0, self.maxWidth - 1), random.randint(0, self.maxHeight - 1)]

      if(self.coordinateCollision("flask", "player")):
         self.placeFlask()
      elif(self.coordinateCollision("flask", "trap")):
         self.placeFlask()
      elif(self.coordinateCollision("flask", "monster")):
         self.placeFlask()
      else:
         return True
      return True

   def checkBoundry(self, newX, newY):
      minWidth = 0
      minHeight = 0

      if(newX < minWidth or newX == self.maxWidth or newY < minHeight or newY == self.maxHeight):
         return False
      else:
         return True 

   def playerMove(self, choice):
      currentX = self.characterPosition[0]
      currentY = self.characterPosition[1]

      if(choice == "W" or choice == "w"):
         if(self.checkBoundry(currentX, currentY-1) == False):
            return False
         else:
            self.characterPosition = [currentX, currentY - 1]
            return True
      elif(choice == "A" or choice == "a"):
         if(self.checkBoundry(currentX - 1, currentY) == False):
            return False
         else: 
            self.characterPosition = [currentX - 1, currentY]
            return True

      elif(choice == "S" or choice == "s"):
         if(self.checkBoundry(currentX, currentY + 1) == False):
            return False
         else:
            self.characterPosition = [currentX, currentY + 1]
            return True

      elif(choice == "D" or choice == "d"):
         if(self.checkBoundry(currentX +1, currentY) == False):
            return False
         else:
            self.characterPosition = [currentX +1, currentY]
            return True 


   def collisionCheck(self):
      if(self.coordinateCollision("player", "monster")):
         self.characterAlive = False
         return True
      elif(self.coordinateCollision("player", "flask")):
         self.characterWon = True
         return True
      elif(self.coordinateCollision("player", "trap")):
         self.monsterAwakened = True
         self.trapPosition = [-1,-1]
         return True

   def coordinateCollision(self, coord1, coord2):

      if(coord1 == "monster"): 
         first = self.monsterPosition
      elif(coord1 == "flask"): 
         first = self.flaskPosition
      elif(coord1 == "trap"):
         first = self.trapPosition
      elif(coord1 == "player"):
         first = self.characterPosition
      else: 
         return None

      if(coord2 == "monster"):
         second = self.monsterPosition
      elif(coord2 == "flask"):
         second = self.flaskPosition
      elif(coord2 == "trap"):
         second = self.trapPosition
      elif(coord2 == "player"):
         second = self.characterPosition
      else:
         return None

      if(coord1 == coord2):
         return None

      if(first[0] == second[0] and first[1] == second[1]):
         return True
      else:
         return False

   def displayMenu(self):
      
      menuList = ["Start New Game", "[Save Game]", "[Load Game]", "Customize Setup", "Exit"]

      print("Type the number of your choice\n")

      for i in range(1, len(menuList) + 1):
         print( str(i) + " " + menuList[i - 1])

      choice = input('Your choice:')
      self.menuChoice(choice)

   def startNewGame(self):
      self.resetAllSettings()
      self.resetCurrentGame()
      self.setupGame()

   def setupGame(self):
      self.placeCharacter()
      self.placeFlask()
      self.placeTrap()
      self.placeMonster()
      self.drawGrid()

   def menuChoice(self, userChoice):
      try:
         choice = int(userChoice)

      except ValueError:
         choice = 0

      if(choice == 1):
         self.startNewGame()

      elif(choice == 2):
         pass

      elif(choice == 3):
         pass

      elif(choice == 4):
         self.createSetup()

      elif(choice == 5):
         sys.exit(0)

      else:
         print("wrong input. Try again")
         self.displayMenu()

   def createSetup(self):
      self.resetAllSettings()
      print("This option lets you set the options for the mosnter")
      widthChoice = input("How wide do you want the game board to be? (Default : 5)")

      try: 
         widthChoice = int(widthChoice)
      except ValueError:
         widthChoice = 5

      self.maxWidth = widthChoice
      heightChoice = input("how high do you want the game board to be? ( default : 5)")

      try:
         heightChoice = int(heightChoice)
      except ValueError:
         heightChoice = 5

      self.maxHeight = heightChoice

      monsterMoveCountChoice = input("How many moves should the moster make? (default: 2)")

      try:
         monsterMoveCountChoice = int(monsterMoveCountChoice)
      except ValueError:
         monsterMoveCountChoice = 5

      self.monsterMovePerTurn = monsterMoveCountChoice      
      self.setupGame()


   def moveMonster(self):
      movesLeft = self.monsterMovePerTurn

      while(movesLeft > 0):
         monX = self.monsterPosition[0]
         monY = self.monsterPosition[1]
         playerX = self.characterPosition[0]
         playerY = self.characterPosition[1]

         if(playerX - monX !=0):
            if(playerX - monX < 0):
               self.monsterPosition = [moX - 1, monY]
            else:
               self.monsterPosition = monX + 1, monY]
         else:
            if(playerY - monY < 0):
               self.monsterPosition = [monX, monY -1]
            else:
               self.monsterPosition = [monX, monY + 1]
         movesLeft = movesLeft -1

   def drawGrid(self):
      
      if(self.characterWon == True):
         print("you have beaten the monster. Congratulations!")
         choice = input("press any key to return to the menu, or press enter to exit")

         if(choice):
            self.displayMenu()

      elif(self.characterAlive == False):
         print("You have been beaten by the monster. Date to try again?")
         choice = input("Try again?")
      else: 

         height = self.maxHeight
         width = self.maxWidth

         for y in range(0, height):
            for x in range(0, width):

               y = str(y)
               x = str(x)

               charX = str(self.characterPosition[0])
               charY = str(self.characterPosition[1])

               if( str(self.monsterPosition[0]) == x and str(self.monsterPosition[1]) == y and self.monsterAwake == True ):
                  sys.stdout.write("M")

               elif(charX == x and charY == y):
                  sys.stdout.write("X")

               else: 
                  sys.stdout.write("?")

            sys.stdout.write("\r\n")
         print("\n move using WASD")
         choice = input("move: ")

         if(self.playerMove(choice) == False):
            print("Not a valid move")
            self.drawGrid()
         else:
            if(self.monsterAwake == True):
               self.moveMonster()
            if(self.collisionCheck() == True):
               if(self.monsterAwakened == True):
                  print("You woke the monster")
                  self.monsterAwake = True
                  self.monsterAwakened == False

         self.drawGrid()


monster = Main()
