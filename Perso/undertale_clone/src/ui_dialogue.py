import pygame

class DialogueBox:
    def __init__(self, width, height, font_size=20):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, font_size)
        self.box_rect = pygame.Rect(20, height - 140, width - 40, 120)
        self.active = False
        self.text = ""
        self.displayed_text = ""
        self.char_index = 0
        self.text_speed = 2  # how fast text appears
        self.frame_count = 0

    def start(self, text):
        """Activate the dialogue box with a given text"""
        self.active = True
        self.text = text
        self.displayed_text = ""
        self.char_index = 0
        self.frame_count = 0

    def update(self):
        """Typewriter text effect"""
        if self.active and self.char_index < len(self.text):
            self.frame_count += 1
            if self.frame_count % self.text_speed == 0:
                self.char_index += 1
                self.displayed_text = self.text[:self.char_index]

    def draw(self, screen):
        """Draw the dialogue box and text"""
        if not self.active:
            return

        # Draw black box
        pygame.draw.rect(screen, (0, 0, 0), self.box_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.box_rect, 2)

        # Render text
        wrapped_text = self.wrap_text(self.displayed_text, self.box_rect.width - 20)
        y_offset = self.box_rect.top + 15

        for line in wrapped_text:
            rendered = self.font.render(line, True, (255, 255, 255))
            screen.blit(rendered, (self.box_rect.left + 15, y_offset))
            y_offset += self.font.get_height() + 5

    def wrap_text(self, text, max_width):
        """Split text into multiple lines if too long"""
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            if self.font.size(test_line)[0] < max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        return lines

    def close(self):
        """Hide the dialogue box"""
        self.active = False