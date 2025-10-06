import pygame
pygame.init()

class Game:

    def __init__(self):
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("PirateQuest")
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.evet.get():
                if event.type == pygame.QUIT:
                    self.running = False
        pygame.quit()


game = Game()
game.run()