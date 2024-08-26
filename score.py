import pygame


class Score:
    def __init__(self, font_size=36, color="white", position=(10,10)):
        self.score = 0
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.position = position

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text,self.position)

    def increase(self, amount = 10):
        self.score += amount
