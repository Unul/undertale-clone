import pygame

class BattleMenu:
    def __init__(self, width, height, font_size=24):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, font_size)
        self.box_rect = pygame.Rect(20, height - 140, width - 40, 120)
        self.options = ["FIGHT", "ACT", "ITEM", "MERCY"]
        self.selected_index = 0
        self.active = False

    def start(self):
        self.active = True
        self.selected_index = 0

    def update(self, events):
        if not self.active:
            return

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key == pygame.K_RIGHT:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    return self.options[self.selected_index]  # returns selected option
        return None

    def draw(self, screen):
        if not self.active:
            return

        # Create a semi-transparent surface
        menu_surface = pygame.Surface((self.box_rect.width, self.box_rect.height))
        menu_surface.set_alpha(180)  # semi-transparent
        menu_surface.fill((0, 0, 0))
        screen.blit(menu_surface, (self.box_rect.left, self.box_rect.top))

        # Draw white border
        pygame.draw.rect(screen, (255, 255, 255), self.box_rect, 2)

        # Draw options
        spacing = 10
        x = self.box_rect.left + 15
        y = self.box_rect.top + 15
        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)
            text_surf = self.font.render(option, True, color)
            screen.blit(text_surf, (x, y))
            x += text_surf.get_width() + spacing