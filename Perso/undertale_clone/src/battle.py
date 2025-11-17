import pygame
import random

class Battle:
    def __init__(self, player, enemy_hp, combat_area):
        self.player = player
        self.enemy_stats = {"hp": enemy_hp}
        self.active = True
        self.action_text = ""
        self.action_timer = 0
        self.projectiles = []
        self.combat_area = combat_area

    def update(self, events):
        # --- Action text timer ---
        if self.action_timer > 0:
            self.action_timer -= 1
        else:
            self.action_text = ""

        # --- Spawn projectiles randomly ---
        if random.randint(0, 20) == 0:
            self.spawn_projectile()

        # --- Move projectiles and check collision ---
        player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
        for proj in self.projectiles[:]:
            proj["y"] += proj["speed"]
            proj_rect = pygame.Rect(proj["x"], proj["y"], proj["size"], proj["size"])
            if not self.combat_area.colliderect(proj_rect):
                self.projectiles.remove(proj)
            elif player_rect.colliderect(proj_rect):
                self.player.hp -= 1
                self.projectiles.remove(proj)

        # --- End battle if HP zero ---
        if self.enemy_stats["hp"] <= 0 or self.player.hp <= 0:
            self.active = False

    def spawn_projectile(self):
        x = random.randint(self.combat_area.left, self.combat_area.right - 10)
        self.projectiles.append({"x": x, "y": self.combat_area.top, "size": 10, "speed": 3})

    def draw(self, screen):
        # Draw player
        pygame.draw.rect(screen, self.player.color, (self.player.x, self.player.y, self.player.width, self.player.height))

        # Draw projectiles
        for proj in self.projectiles:
            pygame.draw.rect(screen, (0, 255, 0), (proj["x"], proj["y"], proj["size"], proj["size"]))
