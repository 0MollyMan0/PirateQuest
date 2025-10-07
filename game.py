import pygame
pygame.init()
from map import MapManager

class Game:

    def __init__(self):
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("PirateQuest")

        self.map_manager = MapManager(self.screen_size)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill((0, 0, 0))
            self.map_manager.render(self.screen, (0,0))
            pygame.display.flip()
        pygame.quit()


game = Game()
game.run()