import pygame
import random

#cree une classe qui va gerer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 545
        self.velocity = 1

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si son nombre de vie est <= 0
        if self.health <= 0:
            #reaparaitre l'entiter
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health


    def update_health_bar(self, surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111,210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity