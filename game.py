import pygame
from player import Player
from monster import Monster

#cree un class qui va representer notre jeu
class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        # charger notre joueur
        self.player = Player(self)
        self.all_players.add(self.player)
        #group de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
