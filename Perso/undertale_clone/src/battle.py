import pygame
import random

class Battle:
    def __init__(self, player_stats, enemy_stats):
        self.player_stats = player_stats
        self.enemy_stats = enemy_stats
        self.active = True
        self.menu = None
        self.action_text = ""
        self.action_timer = 0  # for showing attack text temporarily

    def update(self, events):
        # End battle if HP <= 0
        if self.player_stats["hp"] <= 0 or self.enemy_stats["hp"] <= 0:
            self.active = False
            return

        # Handle simple temporary ESC exit
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.active = False

        # Handle attack text timer
        if self.action_timer > 0:
            self.action_timer -= 1
            if self.action_timer <= 0:
                self.action_text = ""

    def player_attack(self):
        damage = random.randint(5, 12)
        self.enemy_stats["hp"] -= damage
        self.action_text = f"You dealt {damage} damage!"
        self.action_timer = 60  # show text for ~1 second at 60 FPS

    def draw(self, screen):
        # Background
        screen.fill((0, 0, 0))

        # HP bars above menu
        pygame.draw.rect(screen, (255, 0, 0), (50, 50, self.player_stats["hp"]*2, 20))   # Player
        pygame.draw.rect(screen, (0, 0, 255), (400, 50, self.enemy_stats["hp"]*2, 20))   # Enemy

        # Player & Enemy labels
        font = pygame.font.Font(None, 24)
        screen.blit(font.render(f"Player HP: {self.player_stats['hp']}", True, (255,255,255)), (50,25))
        screen.blit(font.render(f"Enemy HP: {self.enemy_stats['hp']}", True, (255,255,255)), (400,25))

        # Action text slightly below bars
        if self.action_text:
            action_font = pygame.font.Font(None, 28)
            screen.blit(action_font.render(self.action_text, True, (255, 255, 0)), (50, 90))