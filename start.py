import pygame
from pygame.locals import *
import json

pygame.init()
width, height = 680, 425
screen=pygame.display.set_mode((width, height))


bg = pygame.image.load("bg.jpg")



class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
class button2():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


def redrawWindow():
    screen.blit(bg, (0,0))
    greenButton.draw(screen, (0,0,0))
    hscoreButton.draw(screen, (0,0,0))
def loadfile(x,y):
    f=open('data.json',)
    data= json.load(f)
    for i in data['score']:
        score_value = 0
        score=font.render("Score: " +str(score_value), True, (255,255, 255))
        screen.blit(score, (x,y))
    f.close()
    

font = pygame.font.Font('freesansbold.ttf',32)
textX = 270
textY = 120


hscoreButton=button2((200,100, 120), 350, 330, 150, 40, 'High Score')
greenButton=button((200,100,120), 150, 330, 100, 40, 'START') #this is for start button
while 1:

    pygame.display.flip()
    redrawWindow()
    pygame.display.update()
    for event in pygame.event.get():
        pos= pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton.isOver(pos):
                print('Clicked')
        if event.type == pygame.MOUSEMOTION:
            if greenButton.isOver(pos):
                greenButton.color=(200,100,120)
            else:
                greenButton.color=(100,200,120)
        if event.type == pygame.MOUSEBUTTONDOWN:
             if hscoreButton.isOver(pos):
                 loadfile(textX, textY)

        if event.type == pygame.MOUSEMOTION:
             if hscoreButton.isOver(pos):
                hscoreButton.color=(200,100,120)
             else:
                hscoreButton.color=(100,200,120)
        
