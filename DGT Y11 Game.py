# Version 1.2
# TODO: Fix the settings menu so that it does not freeze up.
# Make the back button work.

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
BG = pygame.image.load("Sun (start screen 2.0).png")  # Load the background image

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
    # This is Pygame's way of drawing one surface(image/text) on to another(the main screen surface)



def draw_(player):
    screen.blit(PLAYER_IMG, (player.x, player.y))  # Draw the player image

# Button drawing 
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
    running = True # Cotrol the settings menu loop 
    show_how_to_play = False 
    show_more_info = False 
    music_on = False
    option_font = pygame.font.SysFont("comicsans", 40)
    while running:
        # Event Handling
        for event in pygame.event.get():
            #This iterates through 遍历  all the events in the event queue 队列
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Check if the back button is clicked
                # If true: the settings menu will close and return to the main menu
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_btn.collidepoint(event.pos):
                        #print("Back button clicked")
                    #Test if the click position(event.pos) is within the button's rectangle
                        running = False
        screen.fill((30, 30, 30)) # background color
        font = pygame.font.SysFont("comicsans", 45)
        title = font.render("Settings", True, (255, 255, 0))
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 100))
        # The first argument 参数(title) is the text to be rendered 表达,
        #  the second argument is (x,y) specifying where to draw it,
        #  Position Calculation: 
        # (screen.get_width()//2 : Gets half of the screen's width (integer division整除法)
        # title.get_width()//2 ： Gets half of the text surface's width (also integer division)
        # (screen.get_width()//2 - title.get_width()//2) : This calculates the x-coordinate for centering the text on the screen.
        #                                                  It works by finding the screen's center point, then subtracting half the text width
        #The 100 is the y-coordinate where the text will be drawn
    
        if not show_how_to_play and not show_more_info:
           how_to_play_text = font.render("How to Play", True, (100, 200, 250))
           how_to_play_rect = how_to_play_text.get_rect(center=(screen.get_width()//2, 250))
           screen.blit(how_to_play_text, how_to_play_rect)

           more_info_text = font.render("More Info", True, (100, 200, 255))
           more_info_rect = more_info_text.get_rect(center=(screen.get_width()//2, 350))
           font = pygame.font.SysFont("comicsans", 60)
           screen.blit(more_info_text, more_info_rect)

           muscic_text = "Music: ON" if music_on else "Music: OFF"
           music_option = font.render(muscic_text, True, (200, 100, 100))
           music_rect = music_option.get_rect(center=(screen.get_width()//2, 450))
           font = pygame.font.SysFont("comicsans", 60)
           screen.blit(music_option, music_rect)

        back_btn = draw_button(screen.get_width()//2 - 100, 600, 200, 50, "BACK", (255,255,0), (0,0,0))
        pygame.display.flip()
        # flip means to update the display inmediately
        if show_how_to_play:
            s = pygame.Surface((700,400 ), pygame.SRCALPHA)
            s.fill((0,0,0,200))
            screen.blit(s, (screen.get_width()//2 - 350,150))
            title = option_font.render("How to Play", True, (250, 250, 0))  # Create a transparent surface
            screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 180))

            instructions = [
                "Here are some helpful tips and tricks.",
                "1, Use keyboard to move Maui online through the road and answer the question to collect the items.",
                "2, Help Maui avoid dangerous things.",
                "If you hit a danger or answer a question wrong, you will have to restart.",    
                "3, Study the level before."
                "You must play the game in order of the levels. For makeingsure you understand all the points to keep going on the next level.",
            ]
            y_offset = 250
            for line in instructions:
                text = font.render(line, True, (255, 255, 255))
                screen.blit(text, (screen.get_width()//2 - text.get_width()//2, y_offset))
                y_offset += 40 

        elif show_more_info:
            s = pygame.Surface((700,400 ), pygame.SRCALPHA)
            s.fill((0,0,0,200))
            screen.blit(s, (screen.get_width()//2 - 350,150))
            title = option_font.render("More Info", True, (250, 250, 0))
            screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 180))

            more_info = [
                "How Maui Slowe the Sun. The sun roared and thrashed in anger. Maui commanded the sun to slow down-'No longer will you dictate the length of out days-from now on you willtravel slowly across the sky!'",
                "After a long and violent fight, and a few more jawbone strikes, the sun finally gave up-'from now on you will travel slowly across the skey!'Maui declared",
            ]
            y_offset = 250
            for line in more_info: 
                text = font.render(line, True, (255, 255, 255))
                screen.blit(text, (screen.get_width()//2 - text.get_width()//2, y_offset))
                y_offset += 40

    
            
           
            
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
                if settings_btn.collidepoint(mouse_pos):
                    settings_menu()
            
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player.x = mouse_x - PLAYER_WIDTH // 2
        player.y = mouse_y - PLAYER_HEIGHT // 2

        draw_bg()
        draw_button(350, 320, 150, 80, "PLAY", (93,169,47), (0,0,0), font_size=60)
        settings_btn = draw_button(350, 700, 200, 50, "SETTINGS", (200,200,200), (0,0,0))
        draw_(player)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
