import pygame
import sys
import random

from pygame import draw
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP
from pygame.time import Clock


pygame.init()

### Global variables and Assets
LENGTH = 500
SQUARE = 50
gamePlaying = True
speed = pygame.time.Clock()
file = open('highscore.txt','r')


### Colors 
black = (0,0,0)
grey = (160,160,160)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
lightgreen = (52, 155, 2)
darkgreen = (49, 121, 13)
yellow = (252, 211, 4)

### Directions 
UP = (0,-SQUARE)
DOWN = (0,SQUARE)
LEFT = (-SQUARE,0)
RIGHT = (SQUARE,0)
directions = [UP,DOWN,LEFT,RIGHT]
win = pygame.display.set_mode((800,LENGTH))

### Snake
class Snake():
    
    def __init__(self):
        self.curX = SQUARE*random.randrange(0,LENGTH//SQUARE)
        self.curY = SQUARE*random.randrange(0,LENGTH//SQUARE)
        self.rect = pygame.Rect(self.curX,self.curY,SQUARE,SQUARE)
        self.positions = [(self.curX,self.curY)]
        self.curDirection = random.choice(directions)
        self.size = 1

    def get_head(self):
        return self.positions[0]
        
    def move(self):
        speed.tick(10)
        if self.curDirection == UP:
            newX = self.curX % LENGTH
            newY = (self.curY - SQUARE) % LENGTH
            
        if self.curDirection == DOWN:
            newX = self.curX % LENGTH
            newY = (self.curY + SQUARE) % LENGTH
            
        if self.curDirection == RIGHT:
            newX = (self.curX + SQUARE) % LENGTH
            newY = self.curY % LENGTH
            
        if self.curDirection == LEFT:
            newX = (self.curX - SQUARE) % LENGTH
            newY = self.curY % LENGTH

        self.positions.insert(0,(newX,newY))
        self.positions.pop()
        self.curX = newX
        self.curY = newY
            
        
    def turn(self):
        
        keys = pygame.key.get_pressed()
        speed.tick(100)
        if(keys[K_LEFT] and self.curX>0 and self.curDirection != RIGHT):
            self.curDirection = LEFT
        
        if(keys[K_RIGHT] and self.curX<LENGTH and self.curDirection != LEFT):
            self.curDirection = RIGHT

        if(keys[K_UP] and self.curY>0 and self.curDirection != DOWN): 
            self.curDirection = UP   

        if(keys[K_DOWN] and self.curY<LENGTH and self.curDirection != UP):
            self.curDirection = DOWN

    def reset(self):
        self.size = 1
        self.curX = SQUARE*random.randrange(0,LENGTH//SQUARE)
        self.curY = SQUARE*random.randrange(0,LENGTH//SQUARE)
        self.positions = [(self.curX,self.curY)]

    def draw(self):
        for rect in self.positions:
            pygame.draw.rect(win,yellow,(rect[0],rect[1],SQUARE,SQUARE),0)

### Food
class Food():
    def __init__(self):
        self.location = (SQUARE*random.randint(0,LENGTH//SQUARE)%LENGTH,SQUARE*random.randint(0,LENGTH//SQUARE)%LENGTH)
    def draw(self):
       pygame.draw.rect(win, red, (self.location[0],self.location[1],SQUARE,SQUARE), width=0)
    def new_location(self):
        self.location = (SQUARE*random.randint(0,LENGTH//SQUARE) % LENGTH,SQUARE*random.randint(0,LENGTH//SQUARE) % LENGTH)


### Board 
def drawBoard():
    x = 0
    y = 0
    for x in range(LENGTH//SQUARE):
        for y in range(LENGTH//SQUARE):
            if x%2 == 0 and y%2 == 0:
                pygame.draw.rect(win, lightgreen, (x*SQUARE,y*SQUARE,SQUARE,SQUARE), width=0)
            elif x%2 != 0 and y%2 != 0:
                pygame.draw.rect(win, lightgreen, (x*SQUARE,y*SQUARE,SQUARE,SQUARE), width=0)
            else:
                pygame.draw.rect(win, darkgreen, (x*SQUARE,y*SQUARE,SQUARE,SQUARE), width=0)

            
        
            
        
    
def drawScoreBoard(score,highscore):

    image = pygame.image.load("snakegamelogo.png")    
    image = pygame.transform.scale(image,(180, 70))

    scoreBoardScore = pygame.font.SysFont("Comic Sans", 40, bold=True, italic=False)
    scoreBoardHighScore = pygame.font.SysFont("Comic Sans", 40, bold=True, italic=False)

    scoreBoardSurf = scoreBoardScore.render(("Score: "+str(score)), False, white)
    scoreBoardHighScoreSurf = scoreBoardHighScore.render(("High Score: "+str(highscore)),False,white)
    win.blit(scoreBoardSurf,(LENGTH + 90,170))
    win.blit(scoreBoardHighScoreSurf,(LENGTH + 50,200))

    win.blit(image,(LENGTH+60,40))
    win.convert()

def titleScreen():
    image = pygame.image.load("snakegamelogo.png")    
    key = pygame.key.get_pressed()
    titlescreen = True
    welcomeText = pygame.font.SysFont("Comic Sans", 60, bold=False, italic=False)
    welcomeSurf = welcomeText.render(("Welcome to Snakes "), False,white)

    textSurf = welcomeText.render(("Press Space to start "), False,white)

    while titlescreen:
        
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()  
            
            if(event.type == pygame.TEXTINPUT and pygame.K_SPACE):
                titlescreen = False
                
        win.blit(welcomeSurf,(win.get_width() *.25,260))
        win.blit(textSurf,(win.get_width() * .25 ,400))
        win.blit(image,(win.get_width() *.25 ,0))
        win.convert()
        pygame.display.update()
    

def main():
    snake = Snake()
    food = Food()
    highscore = (int) (file.readline())


    while gamePlaying:
        
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
        win.fill(black)
        drawBoard()
        snake.turn()
        snake.move()
        if snake.positions[0] in snake.positions[2:]:
            if (highscore < snake.size):
                with open('highscore.txt','w') as write:
                    highscore = snake.size
                    write.write(str(highscore))
            snake.reset()

        if((snake.curX,snake.curY) == food.location):
            snake.size += 1
            snake.positions.insert(0,food.location)
            food.new_location()
            if(food.location in snake.positions):
                food.new_location()
        
        drawScoreBoard(snake.size,highscore)
        snake.draw()
        food.draw()
        pygame.display.update()
        
titleScreen()

main()

file.close()