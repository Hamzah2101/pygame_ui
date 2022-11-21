def main(x):    #having x as a parameter allows for smooth transition between pages
    ##### set up #####
    import pygame
    import main_menu
    import access
    import modifiers
    import buttons
    import constants
    pygame.init()

    # (self, size_x, size_y, coor_x, coor_y, img) = arguments for creating 'ImgButton' instance
    main_menu_button = buttons.ImgButton(44, 44, 38, 27, 'home (Dave Gandy).png')  # setting button setup
    # Icon made by Dave Gandy from www.flaticon.com

    # (self, size_x, size_y, coor_x, coor_y, text) = arguments for creating 'textButton' instance
    access_button = buttons.TextButton(100, 30, constants.WIDTH - 55, 27, 'access')
    access_button_colour = access_button.get_colour1()

    modifier_button = buttons.TextButton(135, 30, constants.WIDTH - 78, 67, 'modifiers')
    modifier_button_colour = modifier_button.get_colour1()

    clock = pygame.time.Clock()     #variables
    running = True
    mouse_pressed = False
    mouse_timer = 0
    goto_main = False       #if these are set to True, when this loop ends that menu will be started.
    goto_access = False
    goto_modifiers = False

    screen = constants.screen
    pygame.display.set_caption("Hurry!")
    my_icon = constants.my_icon
    background = constants.background
    pygame.display.set_icon(my_icon)


    Title = constants.font65.render('(main menu)', True, constants.WHITE, )
    TitleRect = Title.get_rect()
    TitleRect.center = (constants.WIDTH / 2, 150)

    access_button_text = constants.font25.render(access_button.get_text(), True, constants.BLACK, access_button_colour)
    access_button_textRect = access_button_text.get_rect()
    access_button_textRect.center = (access_button.get_cx(), access_button.get_cy())

    modifier_button_text = constants.font25.render(modifier_button.get_text(), True, constants.BLACK, modifier_button_colour)
    modifier_button_textRect = modifier_button_text.get_rect()
    modifier_button_textRect.center = (modifier_button.get_cx(), modifier_button.get_cy())


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
                    mouse_timer = round(mouse_timer, 3)
                    print("User held mouse for " + str(mouse_timer) + " seconds.")
                    mouse_timer = 0         #only prints mouse button confirmation and durationn after it's let go
                mouse_pressed = False

        ##### processes #####

        if x <= - 8500:
            x = constants.WIDTH + 5  # reset buildings if they go off screen
        x -= 15  # move buildings along

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]  # get mouse position every frame

        if mouse_pressed == True:
            mouse_timer += 1/60

        access_button.activate(mouse_pressed, mouse_x, mouse_y)

        modifier_button.activate(mouse_pressed, mouse_x, mouse_y)

        main_menu_button.activate(mouse_pressed, mouse_x, mouse_y)  # checks whether or not to activate the button

        if main_menu_button.get_activated() == True:
            running = False  # ending loop and then starting next page makes sure multiple
            goto_main = True  # game loops aren't running unnecessarily

        if access_button.get_activated() == True:
            running = False
            goto_access = True

        if modifier_button.get_activated() == True:
            running = False
            goto_modifiers = True

        ##### rendering #####

        screen.fill(constants.DARK_BLUE)

        pygame.draw.circle(screen, constants.NEAR_WHITE, [100, 100], 90, 0)  # moon

        screen.blit(background, (x, -200))

        screen.blit(Title, TitleRect)

        # (screen, [red, blue, green], [left, top, width, height], filled) = arguments for drawing pygame rectangle
        pygame.draw.rect(screen, main_menu_button.colour, [main_menu_button.get_cx() - 24, main_menu_button.get_cy() - 24, 44, 44])
        screen.blit(main_menu_button.get_img(), (main_menu_button.get_cx() - 18, main_menu_button.get_cy() - 18))

        access_button_text = constants.font25.render(access_button.get_text(), True, constants.BLACK, access_button.colour)  # render button
        screen.blit(access_button_text, access_button_textRect)

        modifier_button_text = constants.font25.render(modifier_button.get_text(), True, constants.BLACK, modifier_button.colour)
        screen.blit(modifier_button_text, modifier_button_textRect)

        pygame.display.flip()
        clock.tick(60)

    print("CLosed settings menu.")

    if goto_main == True:
        print("Opened main menu.")
        main_menu.main(x)  # runs main menu

    if goto_access == True:
        print("Opened accessibiltiy menu")
        access.main(x)

    if goto_modifiers == True:
        print("Opened modifiers menu")
        modifiers.main(x)
