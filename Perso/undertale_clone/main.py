import pygame
from src.player import Player
from src.npc import NPC
from src.battle import Battle
from src.ui_dialogue import DialogueBox
import random

# --- Init Pygame ---
pygame.init()
pygame.font.init()
pygame.mixer.init()

# --- Window settings ---
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Undertale Clone Lite")

# --- Clock ---
clock = pygame.time.Clock()
FPS = 60

# --- Game objects ---
player = Player(300, 220)
npc = NPC(400, 220, "Hello traveler! Press E to fight me!")
dialogue_box = DialogueBox(WIDTH, HEIGHT)

# --- Game state ---
game_state = "world"
battle = None

# --- Main loop ---
running = True
while running:
    clock.tick(FPS)
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        # --- Trigger battle when pressing E near NPC ---
        if game_state == "world" and event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            if npc.is_near(player):
                dialogue_box.start("Get ready for battle!")
                dialogue_box.close()
                battle = Battle(player, enemy_hp=50, combat_area=pygame.Rect(50, 50, 540, 200))
                game_state = "battle"

    # --- WORLD STATE ---
    if game_state == "world":
        keys = pygame.key.get_pressed()
        player.update(keys)
        
        if npc.is_near(player):
            if not dialogue_box.active:
                dialogue_box.start(npc.dialogue)
        else:
            if dialogue_box.active:
                dialogue_box.close()

        # --- Draw world ---
        win.fill((50, 50, 50))
        player.draw(win)
        npc.draw(win)
        dialogue_box.update()
        dialogue_box.draw(win)
        pygame.display.flip()

    # --- BATTLE STATE ---
    elif game_state == "battle" and battle is not None:
        keys = pygame.key.get_pressed()
        
        # --- Update player inside combat area ---
        player.update(keys)
        player.x = max(battle.combat_area.left, min(player.x, battle.combat_area.right - player.width))
        player.y = max(battle.combat_area.top, min(player.y, battle.combat_area.bottom - player.height))

        # --- Update battle logic ---
        battle.update(events)

        # --- Draw battle scene ---
        win.fill((30, 30, 30))  # background behind dialogue/combat area
        dialogue_box.update()
        dialogue_box.draw(win)
        battle.draw(win)
        pygame.display.flip()

        # --- End battle ---
        if not battle.active:
            game_state = "world"

pygame.quit()
