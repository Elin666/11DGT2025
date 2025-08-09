# Version 1.3
# TODO: Complete the settings menu

import pygame
import time
import random

# Initialize Pygame
pygame.init()  # Initialize all pygame modules
pygame.font.init()  # Initialize the font module
pygame.mixer.init()  # Initialize the mixer module for sound

# Player settings
PLAYER_VEL = 5
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_IMG = pygame.image.load("Pointer.png")
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT)) 

# Background
BG = pygame.image.load("Sun (start screen 2.0).png")

music_on = True  # Music toggle variable

# Set up the display
screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("Sun Chaser")

# title
title = "Sun Chaser"
title_font = pygame.font.SysFont("comicsans", 60)


def draw_bg():
    screen.blit(BG, (0, 0))  # Draw the background image
    # Render the title text
    title_surface = title_font.render(title, True, (255, 255, 0))  # Yellow color
    title_rect = title_surface.get_rect(center=(screen.get_width() // 2, 60))
    screen.blit(title_surface, title_rect)
    # Draw the settings icon (if loaded)
    if settings_icon:
        screen.blit(settings_icon, (icon_rect.x, icon_rect.y))

def draw_(player):
    screen.blit(PLAYER_IMG, (player.x, player.y)) 

#settings
try:
    settings_icon = pygame.image.load('settings(icon).png')
    settings_icon = pygame.transform.scale(settings_icon, (40, 40))
except FileNotFoundError:
    print('Settings icon not found!')
    settings_icon = None
icon_rect = pygame.Rect(screen.get_width()-50, 10, 40, 40)
 # Draw the settings icon (if loaded)
if settings_icon:
        screen.blit(settings_icon, (icon_rect.x, icon_rect.y))

#button
def draw_button(x, y, w, h, text, color=(255,255,0), text_color=(0,0,0), font_size=35):
    button_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, button_rect, border_radius=10)
    font = pygame.font.SysFont("comicsans", font_size, bold=True)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=button_rect.center)
    screen.blit(text_surf, text_rect)
    return button_rect  # Returns the button rectangle for collision detection

# Settings menu
def settings_menu():
    running = True
    show_how_to_play = False
    show_more_info = False
    global music_on
    option_font = pygame.font.SysFont("comicsans", 40)
    big_font = pygame.font.SysFont("comicsans", 60)
    small_font = pygame.font.SysFont("comicsans", 24)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not show_how_to_play and not show_more_info:
                    if back_btn.collidepoint(event.pos):
                        running = False
                    if how_to_play_rect.collidepoint(event.pos):
                        show_how_to_play = True
                    if more_info_rect.collidepoint(event.pos):
                        show_more_info = True
                    if music_rect.collidepoint(event.pos):
                        music_on = not music_on
                else:
                    # Click anywhere to go back from popups
                    show_how_to_play = False
                    show_more_info = False

        screen.fill((30, 30, 30))

        if not show_how_to_play and not show_more_info:
            title = big_font.render("Settings", True, (255, 255, 0))
            screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 100))
            # Draw options
            how_to_play_text = option_font.render("How to Play", True, (100, 200, 250))
            how_to_play_rect = how_to_play_text.get_rect(center=(screen.get_width()//2, 250))
            screen.blit(how_to_play_text, how_to_play_rect)

            more_info_text = option_font.render("More Info", True, (100, 200, 255))
            more_info_rect = more_info_text.get_rect(center=(screen.get_width()//2, 350))
            screen.blit(more_info_text, more_info_rect)

            music_text = "Music: ON" if music_on else "Music: OFF"
            music_option = option_font.render(music_text, True, (200, 100, 100))
            music_rect = music_option.get_rect(center=(screen.get_width()//2, 450))
            screen.blit(music_option, music_rect)
        elif show_how_to_play:
            s = pygame.Surface((700,400), pygame.SRCALPHA)
            s.fill((0,0,0,200))
            screen.blit(s, (screen.get_width()//2 - 350,150))
            
            # Draw "How to Play" title instead
            popup_title = option_font.render("How to Play", True, (250, 250, 0))
            screen.blit(popup_title, (screen.get_width()//2 - popup_title.get_width()//2, 150))

            instructions = [
                "Here are some helpful tips and tricks.",
                "1. Use keyboard to move Maui online",
                " through the road and answer the question",
                " to collect the items.",
                "2. Help Maui avoid dangerous things.",
                " If you hit a danger or answer a question wrong,",
                " you will have to restart.",    
                "3. Study the level before.",
                " You must play the game in order of the levels.",
                "  For making sure you understand all the points" ,
                " to keep going on the next level.",
            ]
            y_offset = 210
            for line in instructions:
                text = small_font.render(line, True, (255, 255, 255))
                screen.blit(text, (screen.get_width()//2 - text.get_width()//2, y_offset))
                y_offset += 28
        elif show_more_info:
            s = pygame.Surface((700,400), pygame.SRCALPHA)
            s.fill((0,0,0,200))
            screen.blit(s, (screen.get_width()//2 - 350,150))
            
            # Draw "More Info" title instead
            popup_title = option_font.render("More Info", True, (250, 250, 0))
            screen.blit(popup_title, (screen.get_width()//2 - popup_title.get_width()//2, 150))

            more_info = [
                "The Māori are the indigenous people of New Zealand,",
                "with rich oral traditions that explain nature, history,",
                " and values. Their stories often feature Maui,a clever",
                "demigod known for his adventures. ",
                "                                            ",
                "In this game, you will help Maui navigate through",
                " various challenges, learning about Māori culture",
                " and values along the way.",
            ]
            y_offset = 210
            for line in more_info:
                text = small_font.render(line, True, (255, 255, 255))
                screen.blit(text, (screen.get_width()//2 - text.get_width()//2, y_offset))
                y_offset += 28

        back_btn = draw_button(screen.get_width()//2 - 100, 600, 200, 50, "BACK", (255,255,0), (0,0,0))
        pygame.display.flip()
        # flip means to update the display inmediately
       
    
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_btn.collidepoint(event.pos):
                        running = False
                    elif not show_how_to_play and not show_more_info:
                        if how_to_play_rect.collidepoint(event.pos):
                            show_how_to_play = True
                        if more_info_rect.collidepoint(event.pos):
                            show_more_info = True
                        if music_rect.collidepoint(event.pos):
                            music_on = not music_on
                    elif show_how_to_play or show_more_info:
                        if back_btn.collidepoint(event.pos):    
                            show_how_to_play = False
                            show_more_info = False

    
# main loop
def main():
    run = True
    player = pygame.Rect(200, 200, PLAYER_WIDTH, PLAYER_HEIGHT)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if settings button is clicked
                if icon_rect.collidepoint (mouse_pos):
                    settings_menu()
            
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player.x = mouse_x - PLAYER_WIDTH // 2
        player.y = mouse_y - PLAYER_HEIGHT // 2

        draw_bg()
        draw_(player)
        
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()


