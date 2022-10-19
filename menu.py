# menu init

import pygame_menu
from pygame_menu.examples import create_example_window
import pygame
pygame.init()


##def set_difficulty(selected: Tuple, value: Any) -> None:
##    """
##    Set the difficulty of the game.
##    """
##    print(f'Set difficulty to {selected[0]} ({value})')

def onresize(scr, menu):
    window_size = scr.get_size()
    new_w, new_h = window_size[0], window_size[1]
    menu.resize(new_w, new_h)

def RunMenu(screen):
    game_menu = pygame_menu.Menu(
        height=800,
        theme=pygame_menu.themes.THEME_BLUE,
        title='Welcome to the "Hannibal Barca"',
        width=800,
       
    )
    help_menu = pygame_menu.Menu(
        height=800,
        title='Help Menu',
        width=800,
        theme = pygame_menu.themes.THEME_SOLARIZED
    )



    user_name = game_menu.add.text_input('Name: ', default='New Player', maxchar=10)
    ##game_menu.add.selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    game_menu.add.button('Play')
    game_menu.add.button('Help', help_menu)
    game_menu.add.button('Quit', pygame_menu.events.EXIT)
    game_menu.enable()
    while True:
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Mouse detected, button is {event.button}")
                if event.button != 1:
                    continue
                x, y = event.pos
                button = pygame.rect.Rect(375, 400, 50, 50)
                if button.collidepoint(x, y):
                    game_menu.toggle()
            if event.type == pygame.VIDEORESIZE:
                if event.w >= 863 and event.h >= 400:
                    screen = pygame.display.set_mode((event.w, event.h),
                                                      pygame.RESIZABLE)
                    onresize(screen, game_menu)

        if game_menu.is_enabled():
            screen.fill((25, 0, 50))
            game_menu.update(events)
            game_menu.draw(screen)

            pygame.display.flip()
        else:
            break
        


if __name__ == '__main__':
    pass
    
