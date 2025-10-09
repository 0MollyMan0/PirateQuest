import pygame

class Player:

    def __init__(self):
        self.spritesheet = pygame.image.load('assets/spritesheets/characters.png')
        self.frames = []
        self.size = 64

        for i in range(3):
            frame = self.spritesheet.subsurface(pygame.Rect(i * 32, 32, 32, 32))
            frame = pygame.transform.scale(frame, (self.size, self.size))
            self.frames.append(frame)

    def draw(self, surface, screen_size):
        pos = (
            screen_size[0] // 2 - self.size // 2,
            screen_size[1] // 2 - self.size // 2
        )
        frame = self.frames[0]
        surface.blit(frame, pos)