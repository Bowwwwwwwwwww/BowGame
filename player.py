import pygame
from projectile import Projectile
# cree une class qui ve representer notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = 3
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 499

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount




    def launch_projectile(self):
        #cree une nouvelle instance de la classe projectile
        self.all_projectile.add(Projectile(self))

    def update_health_bar(self, surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x +50, self.rect.y + 20, self.max_health, 5])
        pygame.draw.rect(surface, (111,210, 46), [self.rect.x +50, self.rect.y + 20, self.health, 5])


    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #infliger les degats
            self.game.player.damage(self.attack)
    def move_left(self):
        self.rect.x -= self.velocity