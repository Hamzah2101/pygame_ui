def main(x):    #having x as a parameter allows for smooth transition between pages
    ##### set up #####
    import pygame
    import constants
    import buttons
    import main_menu
    import random
    pygame.init()

    red = random.randint(50, 200)
    green = random.randint(50, 200)  #not colour blind friendly
    blue = random.randint(50, 200)

    # (self, name, size_x, size_y, coor_x, coor_y, img) = arguments for creating 'ImgButton' instance
    main_menu_button = buttons.ImgButton(44, 44, constants.WIDTH//2 - 22, 27, 'home (Dave Gandy).png')  # main menu button setup
    # Icon made by Dave Gandy from www.flaticon.com

    main_menu_icon = buttons.ImgButton(44, 44, 200, 280, 'home (Dave Gandy).png')
    main_menu_icon.set_colour([red, green, blue])  #not colour blind friendly
    #main_menu_icon.set_colour(constants.DARK_ORANGE)

    settings_icon = buttons.ImgButton(44, 44, 200, 350, 'settings (dmitri13).png')
    settings_icon.set_colour([red, green, blue])   #not colour blind friendly
    #settings_icon.set_colour(constants.DARK_ORANGE)

    account_icon = buttons.ImgButton(44, 44, 150, 350, 'user (dmitri13).png')
    account_icon.set_colour([red, green, blue])    #not colour blind friendly
    #account_icon.set_colour(constants.DARK_ORANGE)

    leaderboard_icon = buttons.ImgButton(44, 44, 100, 350, 'trophy (dmitri13).png')
    leaderboard_icon.set_colour([red, green, blue])    #not colour blind friendly
    #leaderboard_icon.set_colour(constants.DARK_ORANGE)

    clock = pygame.time.Clock()     #variables
    running = True
    mouse_pressed = False
    mouse_timer = 0
    goto_main = False       #if these are set to True, when this loop ends that menu will be started.

    screen = constants.screen
    pygame.display.set_caption("Hurry!")
    my_icon = constants.my_icon
    background = constants.background
    pygame.display.set_icon(my_icon)

    Title = constants.font65.render('(credits)', True, constants.WHITE)
    TitleRect = Title.get_rect()
    TitleRect.center = (constants.WIDTH / 2, 150)

    Dave_Gandy = "Icon provided by 'Dave Gandy' from 'www.flaticon.com'"
    Dave_Gandy_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(Dave_Gandy, True, constants.RED)
    Dave_Gandy_titleRect = Dave_Gandy_title.get_rect()
    Dave_Gandy_titleRect.center = (414, 280)

    Dmitri13 = "Icons provided by 'Dmitri13' from 'www.flaticon.com'"
    Dmitri13_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(Dmitri13, True, constants.RED)
    Dmitri13_titleRect = Dmitri13_title.get_rect()
    Dmitri13_titleRect.center = (410, 350)

    Nearoo = "Text input boxes used text input library provided by 'Nearoo' on Github."
    Nearoo_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(Nearoo, True, constants.RED)
    Nearoo_titleRect = Nearoo_title.get_rect()
    Nearoo_titleRect.center = (constants.WIDTH//2, 400)

    Alucard = "Background provided by 'Alucard' on 'https://opengameart.org/content/city-background-repetitive-3.'"
    Alucard_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(Alucard, True, constants.RED)
    Alucard_titleRect = Alucard_title.get_rect()
    Alucard_titleRect.center = (constants.WIDTH//2, 430)

    FoxSynergy = "BGM provided by 'FoxSynergy' on 'https://opengameart.org/content/blue-space.'"
    FoxSynergy_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(FoxSynergy, True, constants.RED)
    FoxSynergy_titleRect = FoxSynergy_title.get_rect()
    FoxSynergy_titleRect.center = (constants.WIDTH//2, 460)

    Fupi = "Button sfx provided by 'Fupi' on 'https://opengameart.org/content/8bit-menu-select.'"
    Fupi_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(Fupi, True, constants.RED)
    Fupi_titleRect = Fupi_title.get_rect()
    Fupi_titleRect.center = (constants.WIDTH//2, 490)

    ##### game loop #####
    while running:

        ##### get events #####
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                print("User asked to quit.")
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True
                print("Mouse clicked")
            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_pressed == True:
                    mouse_timer = round(mouse_timer, 4)
                    print("User held mouse for " + str(mouse_timer) + " seconds.")
                    mouse_timer = 0         #only prints mouse button confirmation and duration after it's let go
                mouse_pressed = False

        ##### processes #####

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]  # get mouse position every frame

        if mouse_pressed == True:
            mouse_timer += 1 / 60

        main_menu_button.activate(mouse_pressed, mouse_x, mouse_y)  # checks whether or not to activate the button

        if main_menu_button.get_activated() is True:
            running = False  # ending loop and then starting next page makes sure multiple
            goto_main = True  # game loops aren't running unnecessarily


        if x <= - 8500:
            x = constants.WIDTH + 5  # reset buildings if they go off screen
        x -= 15  # move buildings along

        red = random.randint(50, 200)
        green = random.randint(50, 200)
        blue = random.randint(50, 200)                     #not colour blind friendly
        main_menu_icon.set_colour([red, green, blue])
        settings_icon.set_colour([red, green, blue])
        account_icon.set_colour([red, green, blue])
        leaderboard_icon.set_colour([red, green, blue])

        ##### rendering #####

        screen.fill(constants.DARK_BLUE)

        pygame.draw.circle(screen, constants.NEAR_WHITE, [100, 100], 90, 0)  # moon

        screen.blit(background, (x, -200))

        screen.blit(Title, TitleRect)

        screen.blit(Dave_Gandy_title, Dave_Gandy_titleRect)

        screen.blit(Dmitri13_title, Dmitri13_titleRect)

        screen.blit(Alucard_title, Alucard_titleRect)

        screen.blit(FoxSynergy_title, FoxSynergy_titleRect)

        screen.blit(Fupi_title, Fupi_titleRect)

        screen.blit(Nearoo_title, Nearoo_titleRect)

        # (screen, [red, blue, green], [left, top, width, height], filled) = arguments for drawing pygame rectangle
        pygame.draw.rect(screen, main_menu_button.colour, [main_menu_button.get_cx() - 24, main_menu_button.get_cy() - 24, 44, 44])
        screen.blit(main_menu_button.get_img(), (main_menu_button.get_cx() - 18, main_menu_button.get_cy() - 18))

        screen.blit(Title,TitleRect)

        pygame.draw.rect(screen, main_menu_icon.colour, [main_menu_icon.get_cx() - 24, main_menu_icon.get_cy() -24, 44, 44])
        screen.blit(main_menu_icon.get_img(), (main_menu_icon.get_cx() - 18, main_menu_icon.get_cy() - 18))

        pygame.draw.rect(screen, settings_icon.colour, [settings_icon.get_cx() - 24, settings_icon.get_cy() - 24, 44, 44])
        screen.blit(settings_icon.get_img(), (settings_icon.get_cx() - 18, settings_icon.get_cy() - 18))

        pygame.draw.rect(screen, account_icon.colour, [account_icon.get_cx() - 24, account_icon.get_cy() - 24, 44, 44])
        screen.blit(account_icon.get_img(), (account_icon.get_cx() - 18, account_icon.get_cy() - 18))

        pygame.draw.rect(screen, leaderboard_icon.colour, [leaderboard_icon.get_cx() - 24, leaderboard_icon.get_cy() - 24, 44, 44])
        screen.blit(leaderboard_icon.get_img(), (leaderboard_icon.get_cx() - 18, leaderboard_icon.get_cy() - 18))

        pygame.display.flip()
        clock.tick(60)

    print("Closed credits menu.")  # ends this process and starts the next

    if goto_main == True:
        print("Opened main menu.")
        main_menu.main(x)  # runs main_settings menu