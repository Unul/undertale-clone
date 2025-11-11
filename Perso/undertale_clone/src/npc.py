import pygame

class NPC:
    def __init__(self, x, y, dialogue):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.color = (0, 100, 255)  # bleu
        self.dialogue = dialogue
        self.font = pygame.font.SysFont('Arial', 18)
        self.show_dialogue = False

    def update(self, player):
        # Affiche le dialogue si le joueur est proche
        distance = ((self.x - player.x)**2 + (self.y - player.y)**2) ** 0.5
        self.show_dialogue = distance < 50

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if self.show_dialogue:
            text_surface = self.font.render(self.dialogue, True, (255, 255, 255))
            win.blit(text_surface, (self.x, self.y - 20))