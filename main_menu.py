def main(x):    #having x as a parameter allows for smooth transition between pages
    ##### set up #####
    import pygame
    import constants
    import buttons
    import main_settings
    import account
    import leader_board
    import credits
    pygame.init()


    # (self, size_x, size_y, coor_x, coor_y, img) = arguments for creating 'ImgButton' instance
    settings_button = buttons.ImgButton(44, 44, constants.WIDTH - 33, 27, 'settings (dmitri13).png')          #setting button setup
    # Icon made by Dmitri13 from www.flaticon.com
    account_button = buttons.ImgButton(44, 44, 38, 27, 'user (dmitri13).png')       #acc button setup
    # Icon made by Dmitri13 from www.flaticon.com
    leader_board_button = buttons.ImgButton(44, 44, 38, 76, 'trophy (dmitri13).png')
    # Icon made by DMitri13 from www.flaticon.com

    credits_button = buttons.TextButton(111, 32, constants.WIDTH//2 - 32, constants.HEIGHT - 33, 'credits')
    credits_button_colour = credits_button.get_colour1()

    clock = pygame.time.Clock()     #variables
    running = True
    mouse_pressed = False
    mouse_timer = 0
    goto_settings = False       #if these are set to True, when this loop ends that menu will be started.
    goto_start =False
    goto_account = False
    goto_leader_board = False         #leader_board = leader board
    goto_credits = False
    screen = constants.screen
    pygame.display.set_caption("Hurry!")
    my_icon = constants.my_icon
    background = constants.background
    pygame.display.set_icon(my_icon)

    Title = constants.font100.render('Hurry!', True, constants.WHITE,)
    TitleRect = Title.get_rect()
    TitleRect.center = (constants.WIDTH /2, 150)

    credits_button_text = constants.font25.render(credits_button.get_text(), True, constants.BLACK, credits_button_colour)
    credits_button_textRect = credits_button_text.get_rect()
    credits_button_textRect.center = (credits_button.get_cx(), credits_button.get_cy())

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
            mouse_timer += 1/60

        settings_button.activate(mouse_pressed, mouse_x, mouse_y) #checks whether or not to activate the button

        account_button.activate(mouse_pressed, mouse_x, mouse_y)

        leader_board_button.activate(mouse_pressed, mouse_x, mouse_y)

        credits_button.activate(mouse_pressed, mouse_x, mouse_y)

        if settings_button.get_activated() == True:
            running = False         #ending loop and then starting next page makes sure multiple
            goto_settings = True    #game loops aren't running unnecessarily

        if account_button.get_activated() == True:
            running = False
            goto_account = True

        if leader_board_button.get_activated() == True:
            running = False
            goto_leader_board = True

        if credits_button.get_activated() == True:
            running = False
            goto_credits = True

        if x <= - 8500:
            x = constants.WIDTH + 5     #reset buildings if they go off screen
        x -= 15    #move buildings along

        ##### rendering #####

        screen.fill(constants.DARK_BLUE)

        pygame.draw.circle(screen, constants.NEAR_WHITE, [100, 100], 90, 0)  # moon

        screen.blit(background, (x, -200))

        # (screen, [red, blue, green], [left, top, width, height], filled) = arguments for drawing pygame rectangle
        pygame.draw.rect(screen, settings_button.colour, [settings_button.get_cx() - 24, settings_button.get_cy() - 24, 44, 44])
        screen.blit(settings_button.get_img(), (settings_button.get_cx()- 18, settings_button.get_cy() - 18))

        pygame.draw.rect(screen, account_button.colour, [account_button.get_cx() - 24, account_button.get_cy() - 24, 44, 44])
        screen.blit(account_button.get_img(), (account_button.get_cx() - 18, account_button.get_cy() - 18))

        pygame.draw.rect(screen, leader_board_button.colour, [leader_board_button.get_cx() - 24, leader_board_button.get_cy() - 24, 44, 44])
        screen.blit(leader_board_button.get_img(), (leader_board_button.get_cx() - 18, leader_board_button.get_cy() -18))

        credits_button_text = constants.font25.render(credits_button.get_text(), True, constants.BLACK, credits_button.colour)
        screen.blit(credits_button_text, credits_button_textRect)

        screen.blit(Title, TitleRect)

        pygame.display.flip()
        clock.tick(60)

    print("Closed main menu.")   #ends this process and starts the next

    if goto_settings == True:
        print("Opened settings menu")
        main_settings.main(x)

    if goto_account == True:
        print("Opened account menu")
        account.main(x)

    if goto_leader_board == True:
        print("Opened leader board menu")
        leader_board.main(x)

    if goto_credits == True:
        print("Opended credits menu")
        credits.main(x)
