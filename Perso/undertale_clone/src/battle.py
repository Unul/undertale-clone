import pygame

class Battle:
    def __init__(self, player_stats, enemy_stats):
        # Store stats so the battle loop can access HP
        self.player_stats = player_stats
        self.enemy_stats = enemy_stats
        self.active = True

    def update(self, events):
        # Temporary: press ESC to exit battle
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.active = False

    def draw(self, screen):
        # Fill background black
        screen.fill((0, 0, 0))

        # Draw simple HP bars
        pygame.draw.rect(screen, (255, 0, 0), (50, 400, self.player_stats["hp"] * 2, 20))
        pygame.draw.rect(screen, (0, 0, 255), (400, 400, self.enemy_stats["hp"] * 2, 20))

        # Draw placeholder text
        font = pygame.font.Font(None, 36)
        text = font.render("BATTLE MODE", True, (255, 255, 255))
        screen.blit(text, (50, 200))