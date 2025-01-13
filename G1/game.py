import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Untitled')
        self.screen = pygame.display.set_mode((640,480))

        self.clock = pygame.time.Clock()
 
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0)) # for transparent background of images

        self.img_pos = [160, 260]
        self.movement = [False, False, False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50) 



    def run(self): 
        while True:
            self.screen.fill((14,219,248))
            self.img_pos[0] += (self.movement[3] - self.movement[2]) * 5 
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5  # bool are converted to 0 or 1, true = 1, false = 0. 1 - 0 = 1, 1 - 1 = 0
            self.screen.blit(self.img, self.img_pos)
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())

            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[2] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1] = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[2] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[3] = False

            if self.movement[0]:
                self.img_pos[1] -= 1
            if self.movement[1]:
                self.img_pos[1] += 1
            if self.movement[2]:
                self.img_pos[0] -= 1
            if self.movement[3]:
                self.img_pos[0] += 1
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()