import constants
import pygame
#print("\nStart buttons file")

class Button:
    def __init__(self, size_x, size_y, coor_x, coor_y):
        self.sx = size_x                # 's' refers to size, 'c' refers to coordinate
        self.sy = size_y                # this is why each has their x and y values
        self.cx = coor_x
        self.cy = coor_y
        self.colour1 = constants.ORANGE
        self.colour2 = constants.MID_ORANGE
        self.colour3 = constants.DARK_ORANGE
        self.x_hover = False
        self.y_hover = False
        self.hover = False  #Represents whether mouse is hovering over button or not
        self.clicked = False
        self.activated = False
        self.colour = self.colour1  #starting colour of button
        self.held_before = False

    def set_clicked(self, value):
        self.clicked = value
    def set_activated(self,value):
        self.activated = value
    def set_colour(self, value):
        self.colour = value
    def set_held_before(self, value):
        self.held_before = value

    def set_hover(self,mouse_x,mouse_y):    #setter for hover, x_hrange and y_hrange (hrange = hover range)

        self.x_hrange = [(self.cx - self.sx / 2), (self.cx + self.sx / 2)]
        self.y_hrange = [(self.cy - self.sy / 2), (self.cy + self.sy / 2)]

        if (mouse_x >= int(self.x_hrange[0])) and (mouse_x <= int(self.x_hrange[1])):
            self.x_hover = True
        else:                                   #if mouse x coordinate is within button x range
            self.x_hover = False     #set xhover attribute to True, otherwise, set it to False

        if (mouse_y >= int(self.y_hrange[0])) and (mouse_y <= int(self.y_hrange[1])):
            self.y_hover = True
        else:                                   #if mouse y coordinate is within button x range
            self.y_hover = False     #set yhover attribute to True, otherwise, set it to False

        if self.x_hover == True and self.y_hover == True:
            self.hover = True
        else:                                   #if both xhover and yhover are True, set hover to True, meaning
            self.hover = False      #that the mouse is hovering over the button

    def set_pressed_colour(self, mouse_x, mouse_y):
        self.set_hover(mouse_x, mouse_y)
        if self.get_hover() == False:
            self.colour = self.colour1
        elif self.get_hover() == True:
            self.colour = self.colour3

    def set_released_colour(self, mouse_x, mouse_y):
        self.set_hover(mouse_x, mouse_y)
        if self.get_hover() == False:
            self.colour = self.colour1
        elif self.get_hover() == True:
            self.colour = self.colour2

    def activate(self, mouse_pressed, mouse_x, mouse_y):
        if mouse_pressed == True:       #held before means that the mouse was held before hovering over the button
            self.set_pressed_colour(mouse_x, mouse_y)
            if self.get_colour() == constants.ORANGE:    #if mouse is held but not on button
                self.set_held_before(True)                #held before is set to True
        elif mouse_pressed == False:
            if self.get_colour() == constants.DARK_ORANGE and self.get_held_before() == False:
                self.set_activated(True)     #if held before is False and the mouse has been released and is hovering, the button is activated
                pygame.mixer.Channel(1).play(constants.button_sfx)
            else:
                self.set_released_colour(mouse_x, mouse_y)
            if self.get_held_before() == True:    #if held before is True and hover is True, held_before is set to False
                if self.get_hover() == True:
                    self.set_held_before(False)



    def get_sx(self):
        return self.sx
    def get_sy(self):
        return self.sy
    def get_cx(self):
        return self.cx
    def get_cy(self):
        return self.cy
    def get_colour1(self):
        return self.colour1
    def get_colour2(self):
        return self.colour2
    def get_colour3(self):
        return self.colour3
    def get_x_hover(self):
        return self.x_hover
    def get_y_hover(self):
        return self.y_hover
    def get_hover(self):
        return self.hover
    def get_clicked(self):
        return self.clicked
    def get_activated(self):
        return self.activated
    def get_colour(self):
        return self.colour
    def get_held_before(self):
        return self.held_before


class TextButton(Button):   #Child class of 'Button'
    def __init__(self, size_x, size_y, coor_x, coor_y, text):
        super().__init__(size_x, size_y, coor_x, coor_y)
        self.text = text

    def get_text(self):
        return self.text           # is a getter method for the 'text' attribute


class ImgButton(Button):        #Child class of 'Button'
    def __init__(self, size_x, size_y, coor_x, coor_y, img):
        super().__init__(size_x, size_y, coor_x, coor_y)
        self.img = img

    def get_img(self):
        return pygame.image.load(self.img)             # is  geatter method for the 'img' attribute

class AcceptButton(TextButton):
    def __init__(self, coor_x, coor_y):
        super().__init__(90, 30, coor_x, coor_y, 'accept')
        self.timer = 0

    def activate(self, mouse_pressed, mouse_x, mouse_y):
        if mouse_pressed == True:       #held before means that the mouse was held before hovering over the button
            self.set_pressed_colour(mouse_x, mouse_y)
            if self.get_colour() == constants.ORANGE:    #if mouse is held but not on button
                self.set_held_before(True)                #held before is set to True
        elif mouse_pressed == False:
            if self.get_colour() == constants.DARK_ORANGE and self.get_held_before() == False:
                self.set_activated(True)     #if held before is False and the mouse has been released and is hovering, the button is activated
                pygame.mixer.Channel(1).play(constants.button_sfx)
            else:
                self.set_released_colour(mouse_x, mouse_y)
            if self.get_held_before() == True:    #if held before is True and hover is True, held_before is set to False
                if self.get_hover() == True:
                    self.set_held_before(False)
        if self.activated == True:
            self.timer += 1
        if self.timer > 1:
            self.activated = False
            self.colour = constants.ORANGE
            self.timer = 0



# #(self, name, size_x, size_y, coor_x, coor_y, img)
#button2 = ImgButton("Button2",10,20,10,20,"img")         # This is just an example to make sure all the classes
#print(button2.get_name())                                # work.
#print(button2.get_sx())
#print(button2.get_sy())
#print(button2.get_cx())
#print(button2.get_cy())
#print(button2.get_img())
#print(button2.get_colour1())
#print(button2.get_colour2())
#print(button2.get_colour3())
