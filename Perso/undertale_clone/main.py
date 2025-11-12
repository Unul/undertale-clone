import pygame
from src.player import Player
from src.npc import NPC
from src.battle import Battle
from src.ui_battle import BattleMenu
from src.ui_dialogue import DialogueBox

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

# Initialize menu inside Battle
if battle and not hasattr(battle, "menu"):
    battle.menu = BattleMenu(WIDTH, HEIGHT)
    battle.menu.start()

# --- Main loop ---
running = True
while running:
    clock.tick(FPS)
    events = pygame.event.get()

    # --- Global events ---
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        # --- Trigger battle when pressing E while dialogue is fully displayed ---
        if game_state == "world" and event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            if dialogue_box.active and dialogue_box.char_index >= len(dialogue_box.text):
                dialogue_box.close()
                player_stats = {"hp": 50}
                enemy_stats = {"hp": 25}
                battle = Battle(player_stats, enemy_stats)
                game_state = "battle"

    # --- WORLD STATE ---
    if game_state == "world":
        keys = pygame.key.get_pressed()
        player.update(keys)
        npc.update(player)

        # --- Show dialogue automatically if near NPC, hide if far ---
        if npc.is_near(player):
            if not dialogue_box.active:
                dialogue_box.start(npc.dialogue)
        else:
            if dialogue_box.active:
                dialogue_box.close()

        # --- Draw world scene ---
        win.fill((50, 50, 50))
        player.draw(win)
        npc.draw(win)
        dialogue_box.update()
        dialogue_box.draw(win)
        pygame.display.flip()

    # --- BATTLE STATE ---
    elif game_state == "battle":
        # Initialize battle menu once
        if not hasattr(battle, "menu"):
            from src.ui_battle import BattleMenu
            battle.menu = BattleMenu(WIDTH, HEIGHT)
            battle.menu.start()

        # Update battle logic
        battle.update(events)  # current battle logic (HP, active flag)

        # Update menu and check selected option
        selected_option = battle.menu.update(events)
        if selected_option == "FIGHT":
            import random
            battle.enemy_stats["hp"] -= random.randint(5, 10)
            print("Player attacks!")
            # Optionally reset menu selection for next turn
            battle.menu.selected_index = 0

        # Draw everything
        battle.draw(win)         # draws background, HP bars, etc.
        battle.menu.draw(win)    # draws modal menu
        pygame.display.flip()

        # --- End battle if enemy HP <= 0 or player HP <= 0 ---
        if not battle.active or battle.enemy_stats["hp"] <= 0 or battle.player_stats["hp"] <= 0:
            game_state = "world"

pygame.quit()