import pygame
from logger import log_state
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.vernum}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initialize game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #initialize player
    player_one = Player(int(x), int(y))

    #create clock
    clock = pygame.time.Clock()
    dt = 0

    #infinite update loop
    while True:
        log_state()

        #X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Screen fill
        screen.fill("black")

        #Draw Player
        player_one.draw(screen)

        #Refresh Display
        pygame.display.flip()
        
        #60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
