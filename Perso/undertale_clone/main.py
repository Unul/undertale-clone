import pygame
from src.player import Player
from src.npc import NPC

# --- Init Pygame ---
pygame.init()
pygame.font.init()
pygame.mixer.init()

# --- Window settings ---
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Undertale Clone Lite")

# --- Music ---
pygame.mixer.music.load("assets/sounds/chiptune_loop.ogg")
pygame.mixer.music.set_volume(0.5)  # volume 50%
pygame.mixer.music.play(-1)  # -1 = loop infini

# --- Clock ---
clock = pygame.time.Clock()
FPS = 60

# --- Player ---
player = Player(300, 220)

# --- NPC ---
npc = NPC(400, 220, "Hello! I'm a NPC!")  # dialogue simple

# --- Main loop ---
running = True
while running:
    clock.tick(FPS)

    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update ---
    keys = pygame.key.get_pressed()
    player.update(keys)
    npc.update(player)


    # --- Draw ---
    win.fill((50, 50, 50))  # Simple background
    player.draw(win)
    npc.draw(win)
    pygame.display.flip()

pygame.quit()