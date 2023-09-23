import pygame
from game import Game
pygame.init()

#ceci est pout tester

#generer la fenetre de notre jeux
pygame.display.set_caption("Bow Game")
screen = pygame.display.set_mode((1080,720))



#importer l'arriere plan de notre jeux
background = pygame.image.load('assets/bg.jpg')

#charger notre jeu
game = Game()


running = True

#boucle tant que running == true
while running:

    #applique l'arriere plan de notre jeux
    screen.blit(background,(0, -200))

    #appliquer l'image de notre joueur
    screen.blit(game.player.image, game.player.rect)

    #recupere les projectiles du joueur
    for projectile in game.player.all_projectile:
        projectile.move()

    #recupere les monstres de notre jeu
    for monster in game.all_monsters:
        monster.forward()

    #appliquer lensemble des images de mon group projectile
    game.player.all_projectile.draw(screen)

    #appliquer l'ensemble des images de mon group de monstres
    game.all_monsters.draw(screen)

    #verifie si le joueur veut aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < 1100:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -30:
        game.player.move_left()




    #mettre a jour l'ecran
    pygame.display.flip()


    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #verifie que l'venement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter si un joueur touche le clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
