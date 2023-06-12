#Load pygame and the exit command
import pygame
from sys import exit
from random import randint

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#function for the score
def display_score():
    current_time = int(pygame.time.get_ticks() / 100) - start_time     #starts at 0 every time
    score_surface = test_font.render(f"{current_time}",False,"black")
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time

#function for moving the obstacles
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6
            screen.blit(hannah_surface,obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] #copies the list, but only the rects that aren't -100
        return obstacle_list
    else:
        return []

#function for collision
def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                obstacle_rect_list.clear()
                game_over.play()
                return False
    return True

#function for player animation
def player_animation():
    global player_surface, player_index
    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

#SETTING UP THE GAME:
pygame.init()   #Initialise pygame
screen = pygame.display.set_mode((800,400))  #Make the window
pygame.display.set_caption("Hannah Attack") #Set title
clock = pygame.time.Clock() #For setting speed of game (framerate)
test_font = pygame.font.Font("Fonts/Pixeltype.ttf", 50)  #Font settings to use in text objects, imported font from folder
game_active = False #variable to be able to move between game and game over scenarios
start_time = 0 #variable for the score timer
score = 0   #variable for the score in the game over screen
music = pygame.mixer.Sound("Sound/music.wav") #background music
music.set_volume(0.4)
music.play(loops = -1)  #-1 loops forever

#import images and fonts to use in the game as surfaces:
space_surface = pygame.image.load("Graphics/Space.jpg").convert()  #convert() not necessary but in theory makes it run better/faster
ground_surface = pygame.image.load("Graphics/ground.png").convert()

#Text at the top, paired with a rectangle to position it in the centre easier
text_surface = test_font.render("My Game", True, "black")   #Text. Arguments are "text", AA true/false, "colour".
text_rect = text_surface.get_rect(center = (400,50))

#hannah's icon. Used in the obstacle_rect_list
hannah_surface = pygame.image.load("Graphics/Hannah.png").convert_alpha()
obstacle_rect_list = []
hannah_sound = pygame.mixer.Sound("Sound/Hannah.mp3")
game_over = pygame.mixer.Sound("Sound/got_you.mp3")

#player's code:
player_walk_1 = pygame.image.load("Graphics/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("Graphics/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1,player_walk_2] #list of the two walks
player_index = 0    #index to switch between the two walks
player_jump = pygame.image.load("Graphics/jump.png").convert_alpha()

player_surface = player_walk[player_index] #putting them together
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

jump_sound = pygame.mixer.Sound('Sound/audio_jump.mp3')
jump_sound.set_volume(0.4)

#Intro screen with new player icon standing there:
player_stand = pygame.image.load("Graphics/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0,2)  #scale the image to 2x bigger (arguments are rotation, then scale multiple)
player_stand_rect = player_stand.get_rect(center = (400,200))   #centres it on the screen

game_name = test_font.render("Hannah Attack",False,"gold")
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render("Press spacebar to play",False,"black")
game_message_rect = game_message.get_rect(midbottom = (400,360))

#Timer for obstacles/game changes
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

#UPDATING THE GAME WINDOW:
while True:
    for event in pygame.event.get():    #Gets all possible inputs from the user
        if event.type == pygame.QUIT:
            pygame.quit()   #The opposite of .init() - closes pygame
            exit() #Stops the whole code including while True loop, requires the import at the top
        
        if game_active:
            #Jumping - if a key is down, if that key is space and the player is on the floor, drop gravity to -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -23 
                    jump_sound.play()
           
            if event.type == obstacle_timer:
                obstacle_rect_list.append(hannah_surface.get_rect(midbottom = (900,randint(320,380))))
                hannah_sound.play()
                pygame.time.set_timer(obstacle_timer, randint(550, 2000))       #Randomises the timer until the next obstacle spawn

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    player_rect.y = 300
                    start_time = int(pygame.time.get_ticks() / 100)    #/100 because get_ticks is in milliseconds and I want tenths of seconds

        
            

    if game_active:
        #Put surface onto the screen:
        screen.blit(space_surface,(0,0))
        #Obtacle movement
        obstacle_movement(obstacle_rect_list)
        
        #Ground
        screen.blit(ground_surface, (0,300))
        score = display_score()
        

        pygame.draw.line(screen,"Gold",(0,20),(800,20),10)  #arguments are surface, colour, start coords, end coords, width
        pygame.draw.rect(screen,"Gold",text_rect.inflate(20,20))    #.inflate increases the x and y edges
        display_score()
        
        #Player code:
        player_gravity += 1     #Gravity value increases by 1 in order to simulate exponential falling (falling faster the longer you fall)
        player_rect.y += player_gravity #Move player by the value of gravity each time
        if player_rect.bottom >= 300:   #Program the floor - if the rectangle bottom is on or below 300,
            player_rect.bottom = 300       #set its value to 300.
        player_animation()
        screen.blit(player_surface, player_rect)
        
        

        #Collision between obstacles and player:
        game_active = collisions(player_rect,obstacle_rect_list)
            
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(game_name,game_name_rect)
        
        score_message = test_font.render(f"Your score was: {score}",False,"gold")
        score_message_rect = score_message.get_rect(center = (400,330))

        #Display the game message if not played yet:
        if score == 0:      
            screen.blit(game_message,game_message_rect)
        #Display the last score if currently playing:
        else:
            screen.blit(score_message,score_message_rect)


    pygame.display.update() #Updates the display with anything done in the while loop
    clock.tick(60)  #Sets the speed (framerate)