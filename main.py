import pygame
import pygame,sys
import random
import time

pygame.display.init()
pygame.font.init()
screen_width=1600
screen_height=900
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Balbis")
background = pygame.image.load("background.jpg").convert()
while 1 == 1:
      screen.blit(background, (0,0))
      pygame.display.update()
      class Character:
            x = 50
            y = 50
            width = 10
            height = 10
            vel = 0.9
            area = width * height
            max_area = 1000000
            score = (max_area - area) /1000

      class Border:
            x = 800
            y = 500
            width = 30
            height = 60
            area = x * y
            hitbox_x = x
            hitbox_y = y

      class FinishLine:
            x = 1500
            y = 0
            width = 10
            height = 1600
            hitbox_x = 1500 - Character.width 

      font = pygame.font.SysFont(None, 100)

      def message_to_screen(msg, color, x, y):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text, [x, y])

      run = True
      while run:
            pygame.time.delay(1)
            for event in pygame.event.get():
                  #Quits Game
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                        Character.x -= Character.vel
                        Character.width += 0.03
                        Character.height += 0.03
            if keys[pygame.K_RIGHT]:
                        Character.x += Character.vel
                        Character.width += 0.03
                        Character.height += 0.03
            if keys[pygame.K_UP]:
                        Character.y -= Character.vel
                        Character.width += 0.03
                        Character.height += 0.03
            if keys[pygame.K_DOWN]:
                        Character.y += Character.vel
                        Character.width += 0.03
                        Character.height += 0.03
                  
            
            Character.area = Character.width * Character.height            

                  
            Character.score = (Character.max_area - Character.area * 2) / 1000
            
            #On Game Win
            FinishLine.hitbox_x = 1500 - Character.width
            if round(Character.x) == round(FinishLine.hitbox_x):
                  message_to_screen("You win!", (3,33,44), 800, 400)
                  message_to_screen("Score: " + str(round(Character.score)), (3,33,44), 800, 340)
                  pygame.display.update()
                  times_run = 0
                  times_run += 1
                  score_data = open("scores.txt", "a")
                  score_data.write("Times Run: " + str(times_run) + "\n")
                  score_data.write("Score For Attempt #" +str(times_run) + ": " + str(round(Character.score)) + "\n")
                  score_data.close()
                  time.sleep(2)
                  run = False
            if round(Character.x) == Border.hitbox_x and round(Character.y) == Border.hitbox_y:
                  run = False
            
                        
            pygame.draw.rect(screen, (0, 0, 255), (Character.x, Character.y, Character.width, Character.height))
            pygame.draw.rect(screen, (25, 100, 93), (FinishLine.x, FinishLine.y, FinishLine.width, FinishLine.height))
            #pygame.draw.rect(screen, (0, 255, 0), (FinishLine.hitbox_x, 10, 5, 10000))
            pygame.display.update()

run = True
