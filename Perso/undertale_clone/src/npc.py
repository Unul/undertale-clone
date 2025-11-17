import pygame

class NPC:
    def __init__(self, x, y, dialogue):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.color = (0, 100, 255)  # blue
        self.dialogue = dialogue
        self.font = pygame.font.SysFont('Arial', 18)
        self.show_dialogue = False

    def update(self, player):
        # Displays the dialogue if the player is nearby
        distance = ((self.x - player.x)**2 + (self.y - player.y)**2) ** 0.5
        self.show_dialogue = distance < 50

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


    def is_near(self, player):
        """Check if the player is close enough to interact or start a battle"""
        distance_x = abs(self.x - player.x)
        distance_y = abs(self.y - player.y)
        return distance_x < 50 and distance_y < 50