import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteriodfield import AsteroidField
from shot import Shot
from score import Score

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots,updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    score = Score()

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updateable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player) and not player.invulnerable:
                player.lives -= 1
                if player.lives > 0:
                    player.respawn()
                else:
                    game_over = True
                # print("Game over!")
                # sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    is_killed = asteroid.split()
                    if is_killed:
                        score.increase()
                    shot.kill()
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        # Render the score text
        score.draw(screen)

        #Render lives
        player.show_score(screen)


        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

    # Game over screen
    font = pygame.font.Font(None,72)
    game_over_text = font.render("Game Over", True, (255,0,0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                                 SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
                                 
    pygame.display.flip()
    
    # Wait for a few seconds before quitting
    pygame.time.wait(3000)


        

if __name__ == "__main__":
    main()

