def main(x):    #having x as a parameter allows for smooth transition between pages
    ##### set up #####
    import pygame
    import constants
    import buttons
    import account
    import text_input_classes
    import validate_username
    import validate_password
    pygame.init()

    # (self, name, size_x, size_y, coor_x, coor_y, img) = arguments for creating 'ImgButton' instance
    account_button = buttons.ImgButton(44, 44, constants.WIDTH - 33, 27, 'user (dmitri13).png')     #account button setup
    # Icon made by Dmitri13 from www.flaticon.com

    # (self, size_x, size_y, coor_x, coor_y, text) = arguments for creating 'textButton' instance
    accept_button = buttons.AcceptButton(constants.WIDTH / 2, 440)
    accept_button_colour = accept_button.get_colour1()

    clock = pygame.time.Clock()     #variables
    running = True
    mouse_pressed = False
    mouse_timer = 0
    goto_acc = False       #if these are set to True, when this loop ends that menu will be started.
    accept = False
    uname_valid = True
    pword_valid = True

    screen = constants.screen
    pygame.display.set_caption("Hurry!")
    my_icon = constants.my_icon
    background = constants.background
    pygame.display.set_icon(my_icon)

    Title = constants.font65.render('(sign in menu)', True, constants.WHITE)
    TitleRect = Title.get_rect()
    TitleRect.center = (constants.WIDTH / 2, 150)

    accept_button_text = constants.font25.render(accept_button.get_text(), True, constants.BLACK, accept_button_colour)
    accept_button_textRect = accept_button_text.get_rect()
    accept_button_textRect.center = (accept_button.get_cx(), accept_button.get_cy())

    username_input_title = pygame.font.SysFont('OCR A EXTENDED', 25).render("Enter username: ", True, [255, 255, 255])
    username_input_titleRect = username_input_title.get_rect()
    username_input_titleRect.center = (480, 310)
    username_invalid = 'Username not found'
    username_invalid_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(username_invalid, True, constants.RED)
    username_invalid_titleRect = username_invalid_title.get_rect()
    username_invalid_titleRect.center = (790, 310)

    password_input_title = pygame.font.SysFont('OCR A EXTENDED', 25).render("Enter password: ", True, [255, 255, 255])
    password_input_titleRect = password_input_title.get_rect()
    password_input_titleRect.center = (480, 350)
    password_invalid = 'Password not found'
    password_invalid_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(password_invalid, True, constants.RED)
    password_invalid_titleRect = password_invalid_title.get_rect()
    password_invalid_titleRect.center = (790, 350)

    username_box = text_input_classes.Text_input_box(600, 300, False, screen, 10)

    password_box = text_input_classes.Text_input_box(600, 340, True, screen, 10)


    ##### game loop #####
    while running:

        ##### get events #####
        events = pygame.event.get()
        for event in events:

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
                    mouse_timer = 0  # only prints mouse button confirmation and duration after it's let go
                mouse_pressed = False

        ##### processes #####

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]  # get mouse position every frame

        username_box.configure(mouse_pressed, mouse_x, mouse_y, events)
        username = username_box.get_text()

        password_box.configure(mouse_pressed, mouse_x, mouse_y, events)
        password = password_box.get_text()

        if mouse_pressed == True:
            mouse_timer += 1 / 60

        account_button.activate(mouse_pressed, mouse_x, mouse_y)  # checks whether or not to activate the button

        accept_button.activate(mouse_pressed, mouse_x, mouse_y)

        if account_button.get_activated() is True:
            running = False  # ending loop and then starting next page makes sure multiple
            goto_acc = True  # game loops aren't running unnecessarily

        if accept_button.get_activated() is True:
            uname_valid = False
            pword_valid = False

        if x <= - 8500:
            x = constants.WIDTH + 5  # reset buildings if they go off screen
        x -= 15  # move buildings along

        ##### rendering #####

        screen.fill(constants.DARK_BLUE)

        pygame.draw.circle(screen, constants.NEAR_WHITE, [100, 100], 90, 0)  # moon

        screen.blit(background, (x, -200))

        screen.blit(Title, TitleRect)


        # (screen, [red, blue, green], [left, top, width, height], filled) = arguments for drawing pygame rectangle
        pygame.draw.rect(screen, account_button.colour, [account_button.get_cx() - 24, account_button.get_cy() - 24, 44, 44])
        screen.blit(account_button.get_img(), (account_button.get_cx() - 18, account_button.get_cy() - 18))
        # not sure why cx and cy didn't for the image coordinates

        accept_button_text = constants.font25.render(accept_button.get_text(), True, constants.BLACK, accept_button.colour)  # render button
        screen.blit(accept_button_text, accept_button_textRect)

        screen.blit(username_input_title, username_input_titleRect)

        screen.blit(password_input_title, password_input_titleRect)

        if uname_valid == False:
            screen.blit(username_invalid_title, username_invalid_titleRect)
        if pword_valid == False:
            screen.blit(password_invalid_title, password_invalid_titleRect)
            screen.blit(password_invalid_title, password_invalid_titleRect)

        username_box.display()

        password_box.display()

        screen.blit(Title,TitleRect)

        pygame.display.flip()
        clock.tick(60)

    print("Closed sign in menu.")  # ends this process and starts the next

    if goto_acc == True:
        print("Opened account menu.")
        account.main(x)  # runs main_settings menu
