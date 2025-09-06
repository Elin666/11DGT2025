# Version 1.5
# TODO: Start the game with maui

import pygame
import sys
print(sys.version)
import math
from pygame.math import Vector2 as vector
import time
import random

# Initialize Pygame
pygame.init()  # Initialize all pygame modules
pygame.font.init()  # Initialize the font module
pygame.mixer.init()  # Initialize the mixer module for sound

#font
font_small = pygame.font.SysFont("comicsans", 20)
font_medium = pygame.font.SysFont("comicsans", 30)
font_big = pygame.font.SysFont("comicsans", 40)

# Player settings
PLAYER_VEL = 5
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_IMG = pygame.image.load("Pointer.png")
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Set up the display
screen = pygame.display.set_mode((900, 800))
TIME_SIZE = 64
ANIMATION_SPEED = 6
pygame.display.set_caption("Sun Chaser")

# Background
BG = pygame.image.load("Sun (start screen 2.0).png")
MINGAME_BG = pygame.image.load("game(bg).png").convert()
MINGAME_BG = pygame.transform.scale(MINGAME_BG, (screen.get_width(), screen.get_height()) )
VICTORY_BG = pygame.image.load("last screen.png").convert()
VICTORY_BG = pygame.transform.scale(VICTORY_BG, (screen.get_width(), screen.get_height()))

# title
title = "Sun Chaser"
title_font = pygame.font.SysFont("comicsans", 60)

# Black hole settings
BLACK_HOLE_POS =(835,460)  
BLACK_HOLE_RADIUS = 25
black_hole_rotation = 0
HOLE_ROTATION_SPEED = 0.1 
suck_progress = 0
HOLE_COLOR = (30, 30, 30)  

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

def draw_black_hole():
    global black_hole_rotation
    black_hole_rotation += 1

    pygame.draw.circle(screen, (0,0,0), BLACK_HOLE_POS, BLACK_HOLE_RADIUS)  # Draw the black hole
    pygame.draw.circle(screen, (30,30,30), BLACK_HOLE_POS, BLACK_HOLE_RADIUS-15)

    for i in range(0,360,45):
        angle = math.radians(i +black_hole_rotation)
        end_x = BLACK_HOLE_POS[0] + BLACK_HOLE_RADIUS * math.cos(angle)
        end_y = BLACK_HOLE_POS[1] + BLACK_HOLE_RADIUS * math.sin(angle)
        pygame.draw.line(screen, (100,100,100), BLACK_HOLE_POS, (end_x, end_y), 2)

    pules = int(5 * math.sin(pygame.time.get_ticks() * 0.005))
    pygame.draw.circle(screen, (80,80,80), BLACK_HOLE_POS, BLACK_HOLE_RADIUS-30 + pules, 2)
    
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
    global music_on, game_started
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
#Game state variables
game_started = False  # Flag to check if the game has started
music_on = True  # Music toggle variable

# Narration content
narrations = {
    1: [
        "Long ago, the sun raced too quickly across the sky.",
        "The people had little time to fish or gather food.",
        "Māui decided to slow the sun, so his people could live and thrive."
    ],
    2: [
        "Māui's courage came from his grandmother's wisdom",
        " and her gift—the magic jawbone.",
        "With the help of his brothers, he wove ropes, ",
        "trapped the sun, and forced it to move more slowly."
    ],
    3: [
        "The story of Māui slowing the sun",
         "is not the only tale of struggle against the burning star.",
        "In Chinese myth, the archer Hou Yi",
        "faced ten suns blazing in the sky at once, scorching the earth.",
        "While Māui used ropes and traps,",
        "Hou Yi used his bow and arrows",
        "to shoot down the extra suns.",
        "Both heroes acted to protect their people",
        "and explain the mysteries of nature.",
        "One story explains the length of days and nights,",
        "the other explains droughts and eclipses.",
        "Across cultures, people told these stories to",
        "make sense of the sky, the seasons, and survival."
    ]
}

def show_narration(level_index):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    lines = narrations.get(level_index + 1, [])  # use get() to avoid KeyError
    index = 0
    running = True

    while running:
        screen.fill(BLACK)
        level_title = f"Level {level_index + 1} - Story"
        #title
        title_surface = font_big.render(level_title, True, YELLOW)
        screen.blit(title_surface, (screen.get_width() // 2 - title_surface.get_width() // 2, 120))
        #current line
        if index < len(lines):
            text_surface = font_medium.render(lines[index], True, WHITE)
            screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2,
                                       screen.get_height() // 2))
        else:
            return  # Finished all narration lines
        #hint
        hint_surface = font_small.render("Click to continue...", True, WHITE)
        screen.blit(hint_surface, (screen.get_width() // 2 - hint_surface.get_width() // 2,
                                   screen.get_height() - 80))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                index += 1
                if index >= len(lines): #story finished
                    running = False

# Game level
def play_level(level_index):
    # 1. Show narration first (if you have it)
    show_narration(level_index)

    # 2. Run the minigame once
    minigame_result = play_minigame()

    # 3. If player fails, retry it
    while not minigame_result:
        show_message("You got hit! Try again!")
        minigame_result = play_minigame()

    # 4. If player survives, move to questions
    for question in levels[level_index]["questions"]:
        show_question(question)
# warning text
def show_message(message, duration=1500):
    screen.fill((30, 30, 30))
    text = font_big.render(message, True, (255, 0, 0))
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(duration)

# Actual game
def play_minigame():
    # Load player image
    player_img = pygame.image.load("Maui2.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (80, 130))  # resize
    
    player_x = screen.get_width() // 2
    player_y = screen.get_height() - 120
    player_speed = 7

    # Dangers
    danger_img = pygame.image.load("Fire.png").convert_alpha()
    danger_img = pygame.transform.scale(danger_img, (60, 60))
    dangers = []
    danger_timer = 0
    
    # Survived time
    clock = pygame.time.Clock()
    survived_time = 0

    while True:
        clock.tick(60)
        screen.blit(MINGAME_BG,(0,0))

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Keep inside screen
        player_x = max(0, min(screen.get_width()-80, player_x))

        # Spawn dangers
        danger_timer += 1
        if danger_timer > 40:
            dangers.append([random.randint(0, screen.get_width()-60), -60])
            danger_timer = 0

        # Move dangers
        for d in dangers:
            d[1] += 5  # fall speed

        # Collision check
        player_rect = pygame.Rect(player_x, player_y, 80, 80)
        for d in dangers:
            danger_rect = pygame.Rect(d[0], d[1], 60, 60)
            if player_rect.colliderect(danger_rect):
                return False  # lost the minigame

        # Remove offscreen dangers
        dangers = [d for d in dangers if d[1] < screen.get_height()]

        # Draw
        screen.blit(player_img, (player_x, player_y))
        for d in dangers:
            screen.blit(danger_img, (d[0], d[1]))

        # Timer
        survived_time += 1
        timer_text = font_small.render(f"Survived: {survived_time//60} sec", True, (255,255,255))
        screen.blit(timer_text, (20,20))

        # Win after 10 seconds
        if survived_time > 600:  
            return True  # won the minigame

        pygame.display.flip()


#Leve question text
levels = [
    # Level 1
    {
        "questions": [
            {
                "text": "Why did Maui slow the sun?",
                "options": [
                    "A. To punish the sun",
                    "B. To make the days longer",
                    "C. To steal the sun's power",
                    "D. To impress the gods"
                ],
                "answer": "B"
            }
        ]
    },
    # Level 2 (2 questions)
    {
        "questions": [
            {
                "text": "Who helped Maui slow the sun?",
                "options": ["A. His mother", "B. His grandmother", "C. His brothers", "D. The God"],
                "answer": "C"
            },
            {
                "text": "Who gifted Maui the magic jawbone?",
                "options": ["A. The god Tane Mahuta", "B. His grandmother", "C. His brothers", "D. The sun itself"],
                "answer": "B"
            }
        ]
    },
    # Level 3 (4 questions)
    {
        "questions": [
            {
                "text": "Who is the main hero?",
                "options": ["A. Rangi / Yan Di", "B. Maui / Xihe", "C. Hina / Hou Yi", "D. Maui / Hou Yi"],
                "answer": "D"
            },
            {
                "text": "How many suns are there in the stories?",
                "options": ["A. 1 / 11", "B.1 / 10", "C. 10 / 12", "D. 0 / 7"],
                "answer": "B"
            },
            {
                "text": "What kind of methods do they use?",
                "options": ["A. Ropes and traps / Bow and arrows",
                            "B. Magic chants / Fire spells",
                            "C. Flooding the sky / Building a tower",
                            "D. Prayers / A giant net"],
                "answer": "A"
            },
            {
                "text": "What's the purpose of the stories?",
                "options": ["A.Warn against greed/Teach archery",
                            "B.Teach fishing/Promote sun worship",
                            "C.Explain diurnal cycle/Explain droughts",
                            "D.Nature damage/Predict weather"],
                "answer": "C"
            }
        ]
    }
]

# Question display
def show_question(question, is_last_question=False):
    running = True
    wrong_message_timer = 0  # Timer to show "Wrong!" message
    while running:
        screen.fill((30, 30, 30))
        q_text = font_medium.render(question["text"], True, (255, 255, 255))
        screen.blit(q_text, (screen.get_width()//2 - q_text.get_width()//2, 100))
        
        option_rects = []
        button_height = 70 if is_last_question else 50
        button_width = 500 if is_last_question else 400
        y_start = 250 if is_last_question else 300

        for i, option in enumerate(question['options']):
            rect = draw_button(screen.get_width()//2 - button_width//2,
                               y_start + i*(button_height + 20),
                               button_width,
                               button_height,
                               option,
                               font_size=20)
            option_rects.append(rect)
        
        # Show "Wrong! Try again" if the timer is active
        if wrong_message_timer > 0:
            wrong_text = font_medium.render("Wrong! Try again", True, (255, 0, 0))
            screen.blit(wrong_text, (screen.get_width()//2 - wrong_text.get_width()//2,
                                     y_start + len(question['options'])*(button_height+20) + 20))
            wrong_message_timer -= 1

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for idx, rect in enumerate(option_rects):
                    if rect.collidepoint(mouse_pos):
                        selected_option = "ABCD"[idx]
                        if selected_option == question["answer"]:
                            return True
                        else:
                            # Wrong answer, show message for a few frames
                            wrong_message_timer = 60  # approx 1 second if running at 60 FPS
def show_victory():
    screen.blit(VICTORY_BG, (0, 0))
    text = font_big.render("Congratulations! All Levels Completed!", True, (30,30,30))
    screen.blit(text,(screen.get_width()//2 - text.get_width()//2,340))
    pygame.display.flip()
    pygame.time.wait(4000)

def game_loop():
    global game_started, suck_progress
    current_level = 0
    print("game_loop: started")
    while current_level < len(levels):
        print(f"Starting leve {current_level}")
        play_level(current_level)
         # Level finished, go to next
        current_level += 1
        
    # All levels done
    show_victory()
    game_started = False
    suck_progress = 0
    print("game_loop: finished")
    return True
   
# Main loop
def main():
    global game_started, suck_progress
    run = True
    player = pygame.Rect(200, 200, PLAYER_WIDTH, PLAYER_HEIGHT)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if icon_rect.collidepoint (mouse_pos):
                    settings_menu()
            
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player.x = mouse_x - PLAYER_WIDTH // 2
        player.y = mouse_y - PLAYER_HEIGHT // 2

        player_center = (player.x + PLAYER_WIDTH // 2, player.y + PLAYER_HEIGHT // 2)
        distance = math.dist(player_center, BLACK_HOLE_POS)
        if distance < BLACK_HOLE_RADIUS:
            suck_progress += 1
            
            player.x += (BLACK_HOLE_POS[0] - player_center[0]) * 0.05
            player.y += (BLACK_HOLE_POS[1] - player_center[1]) * 0.05
            if suck_progress > 30:
                game_started = True
        else:
            suck_progress =0     
       
        draw_bg()

        if not game_started:
            draw_black_hole()
            font  = pygame.font.SysFont("comicsans", 25)
            text = font.render("Guide your runner into the black hole to start", True, (169, 169, 169))
            screen.blit(text, (screen.get_width()//2 - text.get_width()//2, 700))
        
        draw_(player)

        if game_started:
            should_continue = game_loop()
            if not should_continue:
                run = False
            else:
                game_started = False
                suck_progress = 0
        
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

