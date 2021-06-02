import pygame
import sys
import random

from pygame import draw
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from pygame.time import Clock


pygame.init()

LENGTH = 500
SQUARE = 50
gamePlaying = True
speed = pygame.time.Clock()

### Colors 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

### Directions 
UP = (0,-SQUARE)
DOWN = (0,SQUARE)
LEFT = (-SQUARE,0)
RIGHT = (SQUARE,0)
directions = [UP,DOWN,LEFT,RIGHT]
win = pygame.display.set_mode((LENGTH,LENGTH))

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
        if self.curDirection == UP:
            newX = self.curX % LENGTH
            newY = (self.curY - SQUARE) % LENGTH
            
        elif self.curDirection == DOWN:
            newX = self.curX % LENGTH
            newY = (self.curY + SQUARE) % LENGTH
            
        elif self.curDirection == RIGHT:
            newX = (self.curX + SQUARE) % LENGTH
            newY = self.curY % LENGTH
            
        elif self.curDirection == LEFT:
            newX = (self.curX - SQUARE) % LENGTH
            newY = self.curY % LENGTH

        if (newX,newY) in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,(newX,newY))
            self.positions.pop()
            self.curX = newX
            self.curY = newY
            
        
    def turn(self):
        keys = pygame.key.get_pressed()
        
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
            pygame.draw.rect(win,green,(rect[0],rect[1],SQUARE,SQUARE),0)

### Food
class Food():
    def __init__(self):
        self.location = (SQUARE*random.randint(0,LENGTH//SQUARE),SQUARE*random.randint(0,LENGTH//SQUARE))
    def draw(self):
       pygame.draw.rect(win, red, (self.location[0],self.location[1],SQUARE,SQUARE), width=0)
    def new_location(self):
        self.location = (SQUARE*random.randint(0,LENGTH//SQUARE) % LENGTH,SQUARE*random.randint(0,LENGTH//SQUARE) % LENGTH)


### Board 
def drawBoard():
    x = 0
    y = 0
    for x in range(LENGTH):
        pygame.draw.line(win, white, (x*SQUARE,0), (x*SQUARE,LENGTH), width=1)
    for y in range(LENGTH):
        pygame.draw.line(win,white, (0,y*SQUARE),(LENGTH,y*SQUARE),width=1)
        

def main():
    snake = Snake()
    food = Food()
    while gamePlaying:
        speed.tick(5)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
        win.fill(black)
        drawBoard()
        snake.turn()
        snake.move()
        if((snake.curX,snake.curY) == food.location):
            snake.size += 1
            snake.positions.insert(0,food.location)
            food.new_location()
            if(food.location in snake.positions):
                food.new_location()
        snake.draw()
        food.draw()
        pygame.display.update()
        
        
        
main()