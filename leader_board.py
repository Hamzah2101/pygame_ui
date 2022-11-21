def main(x):    #having x as a parameter allows for smooth transition between pages
    ##### set up #####
    import pygame
    import constants
    import buttons
    import main_menu
    import personal_best
    pygame.init()

    # (self, name, size_x, size_y, coor_x, coor_y, img) = arguments for creating 'ImgButton' instance
    main_menu_button = buttons.ImgButton(44, 44, constants.WIDTH - 33, 27, 'home (Dave Gandy).png')  # setting button setup
    # Icon made by Dave Gandy from www.flaticon.com

    # (self, size_x, size_y, coor_x, coor_y, text) = arguments for creating 'textButton' instance
    personal_best_button = buttons.TextButton(120, 30, 70, 20, "personal")

    clock = pygame.time.Clock()     #variables
    running = True
    mouse_pressed = False
    mouse_timer = 0
    goto_main = False       #if these are set to True, when this loop ends that menu will be started.
    goto_personal = False

    screen = constants.screen
    pygame.display.set_caption("Hurry!")
    my_icon = constants.my_icon
    background = constants.background
    pygame.display.set_icon(my_icon)
    Title = constants.font65.render('(Leader board menu)', True, constants.WHITE)
    TitleRect = Title.get_rect()
    TitleRect.center = (constants.WIDTH / 2, 150)

    personal_best_button_text = constants.font25.render(personal_best_button.get_text(), True, constants.BLACK, personal_best_button.colour)
    personal_best_button_textRect = personal_best_button_text.get_rect()
    personal_best_button_textRect.center = (personal_best_button.get_cx(), personal_best_button.get_cy())

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
        personal_best_button.activate(mouse_pressed, mouse_x, mouse_y)

        if main_menu_button.get_activated() is True:
            running = False  # ending loop and then starting next page makes sure multiple
            goto_main = True  # game loops aren't running unnecessarily

        if personal_best_button.get_activated() is True:
            running = False
            goto_personal = True

        if x <= - 8500:
            x = constants.WIDTH + 5  # reset buildings if they go off screen
        x -= 15  # move buildings along

        ##### rendering #####

        screen.fill(constants.DARK_BLUE)

        pygame.draw.circle(screen, constants.NEAR_WHITE, [100, 100], 90, 0)  # moon

        screen.blit(background, (x, -200))

        screen.blit(Title, TitleRect)

        # (screen, [red, blue, green], [left, top, width, height], filled) = arguments for drawing pygame rectangle
        pygame.draw.rect(screen, main_menu_button.colour, [main_menu_button.get_cx() - 24, main_menu_button.get_cy() - 24, 44, 44])
        screen.blit(main_menu_button.get_img(), (main_menu_button.get_cx() - 18, main_menu_button.get_cy() - 18))
        personal_best_button_text = constants.font25.render(personal_best_button.get_text(), True, constants.BLACK, personal_best_button.get_colour())
        screen.blit(personal_best_button_text, personal_best_button_textRect)

        screen.blit(Title,TitleRect)

        pygame.display.flip()
        clock.tick(60)

    print("Closed leaderboard menu.")  # ends this process and starts the next

    if goto_main == True:
        print("Opened main menu.")
        main_menu.main(x)  # runs main_settings menu

    if goto_personal is True:
        print("Opened personal best menu.")
        personal_best.main(x)
