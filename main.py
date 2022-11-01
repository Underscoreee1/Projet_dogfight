from game import Game
import pygame
pygame.init()

#generer la fenêtre
pygame.display.set_caption("Dogfight")
screen = pygame.display.set_mode((1500,800))

bulletSound = pygame.mixer.Sound('assets/laser.wav')

img = pygame.image.load('assets/avion.png')

#charger le jeu
game = Game()

running = True

#boucle du jeu
while running:

    screen.fill((65,99,70))

    vector = [0,0]

    #appliquer l'image du joueur
    screen.blit(game.player.image,game.player.rect)
    
    if game.pressed.get(pygame.K_q) or game.pressed.get(pygame.K_LEFT):
        vector[0] -= 1
    if game.pressed.get(pygame.K_d) or game.pressed.get(pygame.K_RIGHT):
        vector[0] += 1
    if game.pressed.get(pygame.K_z) or game.pressed.get(pygame.K_UP):
        vector[1] -= 1

                
    game.player.move(vector[0],vector[1])
    game.player.update()
    game.playerBulletGroup.draw(screen)
    game.playerBulletGroup.update()

    #mettre à jour l'écran
    pygame.display.flip()


    #condition de sortie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP: 
            game.pressed[event.key] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = game.player.fire()
                game.playerBulletGroup.add(bullet)
                bulletSound.play()