import pygame
import time
import random
 
def message(msg, color):
    mesg = font.render(msg, True, color)
    Window.blit(mesg, [int(Window_width/3), int(Window_height/3)])

def draw_snake(snake_block, sList):
	for x in sList:
		pygame.draw.rect(Window, Col2, [int(x[0]), int(x[1]), int(snake_block), int(snake_block)])

def score(points):
	value = font.render("Score: " + str(points), True, Col3)
	Window.blit(value, [0,0])

def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    x1 = Window_width / 2
    y1 = Window_height / 2
 
    x1_change = 0
    y1_change = 0

    length = 1
    sList = []
 
    foodx = round(random.randrange(0, Window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, Window_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            Window.fill(Col1)
            message("You Lost! Press Q-Quit or C-Play Again", Col3)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= Window_width or x1 < 0 or y1 >= Window_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change
        Window.fill(Col1)
        pygame.draw.rect(Window, Col4, [int(foodx), int(foody), int(snake_block), int(snake_block)])
        sHead = []
        sHead.append(x1)
        sHead.append(y1)
        sList.append(sHead)
        if len(sList) > length:
        	del sList[0]

        for t in sList[:-1]:
        	if t== sHead:
        		game_close = True

        draw_snake(snake_block, sList)
        score(length - 1)
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
        	foodx = round(random.randrange(0, Window_width - snake_block)/10)*10
        	foody = round(random.randrange(0, Window_height - snake_block)/10)*10
        	length = length +1
        	print("Yummy!!")
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()

pygame.init()
 
Col1 = (255, 255, 255)
Col2 = (0, 0, 0)
Col3 = (255, 0, 0)
Col4 = (0, 0, 255)
 
Window_width = 800
Window_height = 600
 
Window = pygame.display.set_mode((Window_width, Window_height))
pygame.display.set_caption('sam ol snake game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 30
 
font= pygame.font.SysFont(None, 30)

gameLoop()