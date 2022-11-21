def main(x):    #having x as a parameter allows for smooth transition between pages
    ##### set up #####
    import pygame
    import constants
    import buttons
    import account
    import text_input_classes
    import validate_username
    import validate_password
    import validate_age
    #import validate_age
    pygame.init()

    # (self, size_x, size_y, coor_x, coor_y, img) = arguments for creating 'ImgButton' instance
    account_button = buttons.ImgButton(44, 44, constants.WIDTH - 33, 27, 'user (dmitri13).png')     #account button setup
    # Icon made by Dmitri13 from www.flaticon.com

    # (self, size_x, size_y, coor_x, coor_y, text) = arguments for creating 'textButton' instance
    accept_button = buttons.AcceptButton(constants.WIDTH/2, 440)
    accept_button_colour = accept_button.get_colour1()

    clock = pygame.time.Clock()     #variables
    running = True
    mouse_pressed = False
    mouse_timer = 0
    goto_acc = False       #if these are set to True, when this loop ends that menu will be started.
    accept = False
    uname_valid = True
    pword_valid = True
    age_valid = True

    screen = constants.screen
    pygame.display.set_caption("Hurry!")
    my_icon = constants.my_icon
    background = constants.background
    pygame.display.set_icon(my_icon)

    Title = constants.font65.render('(sign up menu)', True, constants.WHITE)
    TitleRect = Title.get_rect()
    TitleRect.center = (constants.WIDTH / 2, 150)

    accept_button_text = constants.font25.render(accept_button.get_text(), True, constants.BLACK, accept_button_colour)
    accept_button_textRect = accept_button_text.get_rect()
    accept_button_textRect.center = (accept_button.get_cx(), accept_button.get_cy())

    username_input_title = pygame.font.SysFont('OCR A EXTENDED', 25).render("Enter username: ", True, constants.WHITE)
    username_input_titleRect = username_input_title.get_rect()
    username_input_titleRect.center = (480, 310)
    username_invalid = 'Invalid username, must be 4 - 10 characters'
    username_invalid_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(username_invalid, True, constants.RED)
    username_invalid_titleRect = username_invalid_title.get_rect()
    username_invalid_titleRect.center = (875, 310)

    password_input_title = pygame.font.SysFont('OCR A EXTENDED', 25).render("Enter password: ", True, constants.WHITE)
    password_input_titleRect = password_input_title.get_rect()
    password_input_titleRect.center = (480, 350)
    password_invalid_1 = 'Invalid password, must be 4 - 10 characters with at least 1 symbol,'
    password_invalid_title_1 = pygame.font.SysFont('OCR A EXTENDED', 12).render(password_invalid_1, True, constants.RED)
    password_invalid_titleRect_1 = password_invalid_title_1.get_rect()
    password_invalid_titleRect_1.center = (960, 345)
    password_invalid_2 = ' 1 uppercase letter, 1 lowercase letter, and 1 number'
    password_invalid_title_2 = pygame.font.SysFont('OCR A EXTENDED', 12).render(password_invalid_2, True, constants.RED)
    password_invalid_titleRect_2 = password_invalid_title_2.get_rect()
    password_invalid_titleRect_2.center = (905, 360)

    age_input_title = pygame.font.SysFont('OCR A EXTENDED', 25).render("Enter age: ", True, constants.WHITE)
    age_input_titleRect = age_input_title.get_rect()
    age_input_titleRect.center = (517, 390)
    age_invalid = 'Invalid age, must be  an integer above 0'
    age_invalid_title = pygame.font.SysFont('OCR A EXTENDED', 12).render(age_invalid, True, constants.RED)
    age_invalid_titleRect = age_invalid_title.get_rect()
    age_invalid_titleRect.center = (782, 390)

    details_saved = pygame.font.SysFont('OCR A EXTENDED', 25).render("Details saved", True, constants.GREEN)
    details_savedRect = details_saved.get_rect()
    details_savedRect.center = (constants.WIDTH/2, 440)

    username_box = text_input_classes.Text_input_box(600, 300, False, screen, 10)

    password_box = text_input_classes.Text_input_box(600, 340, False, screen, 10)

    age_box = text_input_classes.Text_input_box(600, 380, False, screen, 3)


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
                    mouse_timer = 0         #only prints mouse button confirmation and duration after it's let go
                mouse_pressed = False

        ##### processes #####

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]  # get mouse position every frame

        username_box.configure(mouse_pressed, mouse_x, mouse_y, events)
        username = username_box.get_text()

        password_box.configure(mouse_pressed, mouse_x, mouse_y, events)
        password = password_box.get_text()

        age_box.configure(mouse_pressed, mouse_x, mouse_y, events)
        age = age_box.get_text()

        if mouse_pressed == True:
            mouse_timer += 1 / 60

        account_button.activate(mouse_pressed, mouse_x, mouse_y)  # checks whether or not to activate the button

        if accept == False:
            accept_button.activate(mouse_pressed, mouse_x, mouse_y)

        if account_button.get_activated() is True:
            running = False  # ending loop and then starting next page makes sure multiple
            goto_acc = True  # game loops aren't running unnecessarily

        if accept_button.get_activated() is True:
            if accept is False:
                uname_valid = False
                pword_valid = False
                age_valid = False
                uname_valid = validate_username.main(username)
                print("username valid is " + str(uname_valid))
                pword_valid = validate_password.main(password)
                print("password valid is " + str(pword_valid))
                age_valid = validate_age.main(age)
                print("age valid is " + str(age_valid))
                if uname_valid == True and pword_valid == True and age_valid == True:
                    accept = True
                    print("All accepted")

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

        if accept == False:
            accept_button_text = constants.font25.render(accept_button.get_text(), True, constants.BLACK, accept_button.colour)  # render button
            screen.blit(accept_button_text, accept_button_textRect)

        screen.blit(username_input_title, username_input_titleRect)

        screen.blit(password_input_title, password_input_titleRect)

        screen.blit(age_input_title, age_input_titleRect)

        if uname_valid == False:
            screen.blit(username_invalid_title, username_invalid_titleRect)
        if pword_valid == False:
            screen.blit(password_invalid_title_1, password_invalid_titleRect_1)
            screen.blit(password_invalid_title_2, password_invalid_titleRect_2)
        if age_valid == False:
            screen.blit(age_invalid_title, age_invalid_titleRect)
        if accept is True:
            screen.blit(details_saved, details_savedRect)

        username_box.display()

        password_box.display()

        age_box.display()

        screen.blit(Title,TitleRect)

        pygame.display.flip()
        clock.tick(60)

    print("Closed sign up menu.")  # ends this process and starts the next

    if goto_acc == True:
        print("Opened account menu.")
        account.main(x)  # runs main_settings menu
