import constants
import pygame
pygame.init()
import pygame_textinput
#print("\nStart txt inputs file")


class Text_input_box:
    def __init__(self, coor_x, coor_y, password, screen, max_length):
        # 's' refers to size, 'c' refers to coordinate of the top left corner
        # this is why each has their x and y values
        self.cx = coor_x
        self.cy = coor_y
        self.surface = screen
        self.max_length = max_length
        self.font = pygame.font.SysFont('Consolas', 20)
        self.input = pygame_textinput.TextInput()
        self.input.max_string_length = max_length
        self.input.font_size = 100
        self.input.password = password
        self.input.font_object = pygame.font.SysFont('Consolas', 20)
        self.input.set_cursor_color(constants.WHITE)
        self.txt_input_surface = self.input.get_surface()
        self.activated = False
        self.outline_colour = constants.ORANGE
        self.first_press = True

    def get_cx(self):
        return self.cx
    def get_cy(self):
        return self.cy
    def get_font(self):
        return self.font
    def get_surface(self):
        return self.txt_input_surface
    def get_activated(self):
        return self.activated
    def get_text(self):
        return self.input.input_string

    def do_update(self, events):
        self.input.update(events)

    def activate(self, mouse_press, mouse_x, mouse_y):
        if mouse_press == True:
            if (mouse_x <= self.cx + ((self.max_length * 12) + 6) and mouse_x >= self.cx) and (mouse_y <= self.cy + 31 and mouse_y >= self.cy):
                self.activated = True
                if self.first_press == True:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('vgmenuselect.wav'))
                self.first_press = False
            else:
                self.activated = False
                self.first_press = True

    def configure(self, mouse_press, mouse_x, mouse_y, events):
        self.activate(mouse_press, mouse_x, mouse_y)
        if self.activated == True:
            self.do_update(events)

    def display(self):
        if self.activated == True:
            pygame.draw.rect(self.surface, constants.ORANGE, [self.cx - 2, self.cy - 2, (self.max_length * 12) + 8, 31])
        pygame.draw.rect(self.surface, constants.WHITE, [self.cx, self.cy, (self.max_length * 12) + 3, 27])
        self.surface.blit(self.input.get_surface(), (self.cx + 4, self.cy + 4))

#print("Test.")
#example = Text_input_box(10,10,False,constants.screen)
#print( example.get_cx() )
#print( example.get_font() )